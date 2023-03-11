from app import app, db
from collections import Counter
from dotenv import load_dotenv
from flask import jsonify, request, Response
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import Pipeline
from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import RandomUnderSampler
from models import SoS, Constituent, Basic_Feature, Emergent_Behavior, SoS_Constituent, Constituent_Basic_Feature, Basic_Feature_Emergent_Behavior, SoS_Emergent_Behavior, User
from numpy import absolute
from numpy import asarray
from numpy import mean
from numpy import std
from sklearn.datasets import make_blobs
from sklearn.datasets import make_multilabel_classification
from sklearn.datasets import make_regression
from sklearn.decomposition import SparsePCA, PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.metrics import classification_report, accuracy_score, f1_score
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, multilabel_confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold, RepeatedKFold, KFold
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.multioutput import RegressorChain
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import NearestNeighbors
from sklearn.svm import LinearSVR, LinearSVC
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils.class_weight import compute_class_weight
from skmultilearn.model_selection import iterative_train_test_split
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.serializer import loads, dumps
from tensorflow.keras.callbacks import Callback,ModelCheckpoint
from tensorflow.keras.layers import Dense, Dropout, Activation, Input
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
import csv
import datetime
import io
import jsons
import jwt
import matplotlib
import matplotlib.pyplot as plt
import nltk
import numpy as np
import os
import pandas as pd
import pathlib
import random
import re
import sklearn
import tensorflow as tf
import json
import tensorflow.keras.backend as K
matplotlib.use('Agg')


load_dotenv()


def processDatabase(logged_user):
    print('Starting process...')
    print('Cleaning session...')
    K.clear_session()

    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
    query_for_pre_processing = os.path.join(ROOT_DIR, 'sql_scripts', 'query_for_pre_processing.sql')
    engine = create_engine(os.environ.get('DATABASE_URL'))
    with engine.connect() as con:
        with open(query_for_pre_processing) as file:
            query = text(file.read())
            # result = con.execute(query)
            df_from_db = pd.read_sql(query, con = con)

    df_from_db = df_from_db.drop_duplicates(keep='first')
    df_from_db = df_from_db.reset_index().drop('index', axis = 1)

    print('Dataset sucessfuly read from db. Initiating pre-process...') 

    sum_groups = 0

    for k, v in df_from_db.groupby((df_from_db['emergent_behavior'].shift() != df_from_db['emergent_behavior']).cumsum()):
        sum_groups += 1

    print('Total of SoS: ', sum_groups)

    constituents_dataset = pd.DataFrame(df_from_db.constituent.dropna().unique(), columns=['constituent'])
    constituents_dataset = constituents_dataset.set_index(list(constituents_dataset)[0]).T
    constituents_dataset = pd.concat([constituents_dataset, pd.DataFrame(0, index=range(sum_groups), columns=constituents_dataset.columns)], ignore_index=True)
    constituents_dataset.index.names = ['SoS']

    emergent_behaviors_dataset = pd.DataFrame(df_from_db.emergent_behavior.dropna().unique(), columns=['emergent_behavior'])
    emergent_behaviors_dataset = emergent_behaviors_dataset.set_index(list(emergent_behaviors_dataset)[0]).T
    emergent_behaviors_dataset = pd.concat([emergent_behaviors_dataset, pd.DataFrame(0, index=range(sum_groups), columns=emergent_behaviors_dataset.columns)], ignore_index=True)
    emergent_behaviors_dataset.index.names = ['SoS']

    for k, v in df_from_db.groupby((df_from_db['emergent_behavior'].shift() != df_from_db['emergent_behavior']).cumsum()):
        print(f'[Line {k-1}]:')
        print('Constituents: ', v['constituent'].values)
        print('Emergent Behavior: ', v['emergent_behavior'].unique())
        print()

        for constituent in v['constituent'].values:
            constituents_dataset.loc[k-1, constituent] = 1
        # constituents_dataset[constituent][k-1] = 1

        # constituents_dataset[v['emergent_behavior'].unique()][k-1] = 1
        emergent_behaviors_dataset.loc[k-1, v['emergent_behavior'].unique()] = 1


    X = constituents_dataset
    y = emergent_behaviors_dataset

    pca = SparsePCA(n_components=10)
    pca.fit(X)
    X_pca = pca.transform(X)

    print("original shape:   ", X.shape)
    print("transformed shape:", X_pca.shape)

    xtrain, xtest, ytrain, ytest = train_test_split(X_pca, y, train_size=0.8, random_state=42)

    print('Lengths of the sets: ', len(xtrain), len(xtest), len(ytrain), len(ytest))

    ts = str(datetime.datetime.now())
    string_replacements = {' ':'T', ':':'_'}

    for (x, y) in string_replacements.items():
        ts = ts.replace(x, y)

    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))

    report_path = pathlib.Path(os.path.join(ROOT_DIR, 'shared', 'classification_reports', ts))
    report_path.mkdir(parents=True, exist_ok=True)

    fig_path = pathlib.Path(os.path.join(ROOT_DIR, 'shared', 'confusion_matrices', ts))
    fig_path.mkdir(parents=True, exist_ok=True)

    # output_columns_binary = []
    dict_dataframes = {}
    errors = 0
    array_models = []
    index = 0

    df_report_labels = pd.DataFrame()
    df_plot_labels = pd.DataFrame()


    # print('Checkpoint 0c...')
    for col_name in ytrain.columns: 

        new_row_matrix = pd.DataFrame({'Index': '{:03}'.format(index), 'Emergent Behavior': col_name}, index=[0])
        df_plot_labels = pd.concat([df_plot_labels.loc[:], new_row_matrix]).reset_index(drop=True)

        try:
            X_train = xtrain               
            y_train = pd.DataFrame(ytrain[col_name])

            newX_train, newy_train = rebalancer(X_train, y_train)

            X_test = xtest
            y_test = pd.DataFrame(ytest[col_name])

            newX_test, newy_test = rebalancer(X_test, y_test)               
            model = LinearSVR()
            wrapper = RegressorChain(model)

            wrapper.fit(newX_train, newy_train)
            print('SCORE FOR: ', col_name)
            print(wrapper.score(newX_train, newy_train))
            print()

            new_row_report = pd.DataFrame({'Index': '{:03}'.format(index), 'Emergent Behavior': col_name, 'Train/Test Score': wrapper.score(newX_train, newy_train)}, index=[0])
            df_report_labels = pd.concat([df_report_labels.loc[:], new_row_report]).reset_index(drop=True)

            yhat = wrapper.predict(newX_test)
            yDF = pd.DataFrame(yhat)

            for i in range(len(yDF)):
                for column in yDF.columns:
                    yDF[column][i] = abs(round(yDF[column][i], 0))
                    if (yDF[column][i] > 1):
                        yDF[column][i] = 1

            yDF.set_index(newy_test.index, inplace=True)
            yDF.columns = newy_test.columns

            print(classification_report(newy_test[col_name], yDF[col_name]))
            print()

            report = classification_report(newy_test[col_name], yDF[col_name], output_dict=True)
            report.update({"accuracy": {"precision": None, "recall": None, "f1-score": report["accuracy"], "support": report['macro avg']['support']}})

            df = pd.DataFrame(report).transpose()

            report_filepath = os.path.join(report_path, 'report_{:03}.csv'.format(index))
            # print('saving report: ', report_filepath)
            df.to_csv(report_filepath)


            y_real = newy_test[col_name]
            y_predito = yDF[col_name]

            confusion_matrix1 = confusion_matrix(y_real, y_predito)
            display = ConfusionMatrixDisplay(confusion_matrix1).plot()
            plt.title(col_name)

            file_path = os.path.join(fig_path, 'matrix_{:03}.png'.format(index))
            # print('saving plot: ', file_path)

            plt.savefig(file_path, bbox_inches='tight')
            plt.close()


            dataframe_data = {}
            dataframe_data['newX_train'] = newX_train
            dataframe_data['newy_train'] = newy_train
            dataframe_data['newX_test'] = newX_test
            dataframe_data['newy_test'] = newy_test
            dataframe_data['model'] = wrapper
            dataframe_data['score'] = wrapper.score(newX_train, newy_train)
            dataframe_data['behavior'] = col_name
            dataframe_data['predictions'] = yDF
            dataframe_data['classification_report'] = classification_report(newy_test[col_name], yDF[col_name])

            array_models.append(dataframe_data)

            index += 1
            # dict_dataframes[col_name] = dataframe_data

        except Exception as e:
            dataframe_data = {}
            dataframe_data['newX_train'] = None
            dataframe_data['newy_train'] = None
            dataframe_data['newX_test'] = None
            dataframe_data['newy_test'] = None
            dataframe_data['model'] = None
            dataframe_data['score'] = 0
            dataframe_data['behavior'] = col_name
            dataframe_data['predictions'] = None
            dataframe_data['classification_report'] = None

            array_models.append(dataframe_data)

            errors += 1
            index += 1
            # print('ERROR AT ', col_name)
            # print(e)
            # print()
            continue


    report_labels_filepath = os.path.join(report_path, 'summary.csv')
    df_report_labels.to_csv(report_labels_filepath)

    plot_labels_filepath = os.path.join(fig_path, 'summary.csv')
    df_report_labels.to_csv(plot_labels_filepath)


    user_file = os.path.join(report_path, 'user.txt')
    with open(user_file, 'w') as f:
        f.write(logged_user)

    user_file = os.path.join(fig_path, 'user.txt')
    with open(user_file, 'w') as f:
        f.write(logged_user)

    print('ERRORS (BEHAVIORS THAT DID NOT ANY SAMPLES FROM ONE OF THE CLASSES (MAYBE CLASS "1")): ', errors)
    print()

    dumps_path = pathlib.Path(os.path.join(ROOT_DIR, 'shared', 'dumps', ts))
    dumps_path.mkdir(parents=True, exist_ok=True)

    dump_sos_path = os.path.join(dumps_path, 'dump_sos')
    dump_constituent_path = os.path.join(dumps_path, 'dump_constituent')
    dump_dump_basicFeature_path = os.path.join(dumps_path, 'dump_basicFeature')
    dump_emergentBehavior_path = os.path.join(dumps_path, 'dump_emergentBehavior')
    dump_sosConstituent_path = os.path.join(dumps_path, 'dump_sosConstituent')
    dump_constituentBasicFeature_path = os.path.join(dumps_path, 'dump_constituentBasicFeature')
    dump_basicFeatureEmergentBehavior_path = os.path.join(dumps_path, 'dump_basicFeatureEmergentBehavior')
    dump_sosEmergentBehavior_path = os.path.join(dumps_path, 'dump_sosEmergentBehavior')

    with open(dump_sos_path, 'wb') as dump_sos:
        dump_sos.write(dumps(db.session.query(SoS.SoS).all()))
    with open(dump_constituent_path, 'wb') as dump_constituent:
        dump_constituent.write(dumps(db.session.query(Constituent.Constituent).all()))
    with open(dump_dump_basicFeature_path, 'wb') as dump_basicFeature:
        dump_basicFeature.write(dumps(db.session.query(Basic_Feature.Basic_Feature).all()))
    with open(dump_emergentBehavior_path, 'wb') as dump_emergentBehavior:
        dump_emergentBehavior.write(dumps(db.session.query(Emergent_Behavior.Emergent_Behavior).all()))
    with open(dump_sosConstituent_path, 'wb') as dump_sosConstituent:
        dump_sosConstituent.write(dumps(db.session.query(SoS_Constituent.SoS_Constituent).all()))
    with open(dump_constituentBasicFeature_path, 'wb') as dump_constituentBasicFeature:
        dump_constituentBasicFeature.write(dumps(db.session.query(Constituent_Basic_Feature.Constituent_Basic_Feature).all()))
    with open(dump_basicFeatureEmergentBehavior_path, 'wb') as dump_basicFeatureEmergentBehavior:
        dump_basicFeatureEmergentBehavior.write(dumps(db.session.query(Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior).all()))
    with open(dump_sosEmergentBehavior_path, 'wb') as dump_sosEmergentBehavior:
        dump_sosEmergentBehavior.write(dumps(db.session.query(SoS_Emergent_Behavior.SoS_Emergent_Behavior).all()))            
        

    user_file = os.path.join(dumps_path, 'user.txt')
    with open(user_file, 'w') as f:
        f.write(logged_user)

    return X, pca, array_models


@app.route('/database/process', methods=['POST'])
def process():
    try:
        token = request.json['token']
        data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])

        user = User.User.query.filter_by(email=data['sub']).first()
        logged_user = user.email

        X, pca, array_models = processDatabase(logged_user)

        return jsonify('SoS saved successfully!')  
    except Exception as e:
        db.session.rollback()
        # print('ERROR => ', e)
        return Response(
                "Internal Server Error: {}".format(e),
                status=500,
            )     

def rebalancer(X, y):
    over = RandomOverSampler(sampling_strategy='minority')
    under = RandomUnderSampler(sampling_strategy='majority')
    steps = [('o', over), ('u', under)]
    pipeline = Pipeline(steps=steps)

    X, y = pipeline.fit_resample(X, y)

    return X, y


@app.route('/predict', methods=['POST'])
def predict():
    class EmergentBehavior():
        def __init__(self, emergent_external_id, description, probability):
            self.emergent_external_id = emergent_external_id
            self.description = description
            self.probability = probability

        def toJSON(self):
            return jsons.dump(self) 

    try:
        token = request.json['token']
        data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])

        user = User.User.query.filter_by(email=data['sub']).first()
        logged_user = user.email

        X, pca, array_models = processDatabase(logged_user)

        new_SoS = np.zeros(len(X.columns))
        newSoS_DF = pd.DataFrame(new_SoS).T
        newSoS_DF.columns = X.columns

        constituents_elements = list(request.json['constituent_list'])

        for i in range(len(constituents_elements)):
            constituent = constituents_elements[i]['constituent_name']
            newSoS_DF.loc[0 , constituent] = 1

        newSoS_PCA = pca.transform(newSoS_DF)

        array_predictions = [] 
        array_predicted_behaviors = []

        for i in range(len(array_models)):
            dict_prediction = {}
            if (array_models[i]['model'] == None):
                continue
                # array_predictions.append(0)
                # print(0)
            else:
                yhat = array_models[i]['model'].predict(newSoS_PCA)
                value = int(round(yhat[0][0]))

                if value == 1:
                    dict_prediction['behavior'] = array_models[i]['behavior']
                    if(yhat[0][0] > 1):
                        dict_prediction['probability'] = 100
                    else:
                        dict_prediction['probability'] = yhat[0][0] * 100
                    
                    array_predictions.append(dict_prediction)
                    array_predicted_behaviors.append(array_models[i]['behavior'])
                    continue
                if value < 0:
                    value = 0
                    continue
                if value > 1:
                    dict_prediction['behavior'] = array_models[i]['behavior']
                    dict_prediction['probability'] = 100
                    array_predictions.append(dict_prediction)
                    array_predicted_behaviors.append(array_models[i]['behavior'])
                    continue


        print('array_predictions => ', array_predictions)
        print()

        print('array_predicted_behaviors => ', array_predicted_behaviors)
        print()


        arr_prediction_obj = []
        for i in range(len(array_predictions)):
            emergent_behaviors_obj = Emergent_Behavior.Emergent_Behavior.query.filter_by(description = array_predictions[i]['behavior']).first()
            probability = round(array_predictions[i]['probability'], 2)
            prediction = EmergentBehavior(emergent_external_id=emergent_behaviors_obj.emergent_external_id, description=emergent_behaviors_obj.description, probability=probability)
            arr_prediction_obj.append(prediction)
        return jsonify([e.toJSON() for e in arr_prediction_obj])
    except Exception as e:
        # print('ERROR => ', e)
        return Response(
                "Internal Server Error: {}".format(e),
                status=500,
            )