from app import app, db
from flask import jsonify, request, Response
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text
from models import SoS, Constituent, Basic_Feature, Emergent_Behavior, SoS_Constituent, Constituent_Basic_Feature, Basic_Feature_Emergent_Behavior, SoS_Emergent_Behavior, User
import os
import datetime
import jsons

import jwt

from tensorflow.keras.callbacks import Callback,ModelCheckpoint
# from tensorflow.keras.layers import Dense, Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Activation, Input
from tensorflow.keras.layers import Dense, Dropout, Activation, Input
# from keras.layers.convolutional import Conv2D
# from tensorflow.keras.layers import Embedding
# from tensorflow.keras.layers.merge import concatenate
# from tensorflow.keras.layers.pooling import MaxPooling2D
from tensorflow.keras.models import Model
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import plot_model
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
# from nltk.corpus import stopwords
# from nltk.stem.wordnet import WordNetLemmatizer
# from nltk.tokenize import word_tokenize
from numpy import asarray
from numpy import mean
from numpy import std
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, accuracy_score, f1_score
# from sklearn.model_selection import GridSearchCV
# from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
# from sklearn.multioutput import MultiOutputClassifier
# from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.utils.class_weight import compute_class_weight
from sqlalchemy import create_engine
import io
import tensorflow.keras.backend as K
import nltk
import numpy as np
import pandas as pd
import re
import tensorflow as tf

import numpy as np
import pandas as pd
import random
# from sklearn.datasets import make_classification
from sklearn.neighbors import NearestNeighbors

from tensorflow.keras.models import load_model

import csv

from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pathlib
from sqlalchemy.ext.serializer import loads, dumps

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
from sklearn.datasets import make_multilabel_classification
from sklearn.svm import SVC
from sklearn.multioutput import MultiOutputClassifier
from sklearn.decomposition import SparsePCA, PCA
import random
from sklearn.datasets import make_classification
from sklearn.neighbors import NearestNeighbors
from numpy import absolute
from numpy import mean
from numpy import std
from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from numpy import mean
from numpy import std
from numpy import absolute
from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.multioutput import RegressorChain
from sklearn.svm import LinearSVR
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import multilabel_confusion_matrix, ConfusionMatrixDisplay
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import Pipeline
import sklearn
from collections import Counter
from sklearn.datasets import make_classification
from numpy import mean
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold, RepeatedKFold, KFold
from sklearn.tree import DecisionTreeClassifier
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from skmultilearn.model_selection import iterative_train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.multioutput import RegressorChain
from sklearn.svm import LinearSVR, LinearSVC
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor

load_dotenv()

# def get_tail_label(df):
#     """
#     Give tail label colums of the given target dataframe
    
#     args
#     df: pandas.DataFrame, target label df whose tail label has to identified
    
#     return
#     tail_label: list, a list containing column name of all the tail label
#     """
#     columns = df.columns
#     n = len(columns)
#     irpl = np.zeros(n)
#     for column in range(n):
#         irpl[column] = df[columns[column]].value_counts()[1]
#     irpl = max(irpl)/irpl
#     mir = np.average(irpl)
#     tail_label = []
#     for i in range(n):
#         if irpl[i] >= mir:
#             tail_label.append(columns[i])
#     return tail_label

# def get_index(df):
#   """
#   give the index of all tail_label rows
#   args
#   df: pandas.DataFrame, target label df from which index for tail label has to identified
    
#   return
#   index: list, a list containing index number of all the tail label
#   """
#   tail_labels = get_tail_label(df)
#   index = set()
#   for tail_label in tail_labels:
#     sub_index = set(df[df[tail_label]==1].index)
#     index = index.union(sub_index)
#   return list(index)

# def get_minority_instace(X, y):
#     """
#     Give minority dataframe containing all the tail labels
    
#     args
#     X: pandas.DataFrame, the feature vector dataframe
#     y: pandas.DataFrame, the target vector dataframe
    
#     return
#     X_sub: pandas.DataFrame, the feature vector minority dataframe
#     y_sub: pandas.DataFrame, the target vector minority dataframe
#     """
#     index = get_index(y)
#     X_sub = X[X.index.isin(index)].reset_index(drop = True)
#     y_sub = y[y.index.isin(index)].reset_index(drop = True)
#     return X_sub, y_sub

# def nearest_neighbour(X):
#     """
#     Give index of 5 nearest neighbor of all the instance
    
#     args
#     X: np.array, array whose nearest neighbor has to find
    
#     return
#     indices: list of list, index of 5 NN of each element in X
#     """
#     nbs=NearestNeighbors(n_neighbors=5,metric='euclidean',algorithm='kd_tree').fit(X)
#     euclidean,indices= nbs.kneighbors(X)
#     return indices

# def MLSMOTE(X,y, n_sample):
#     """
#     Give the augmented data using MLSMOTE algorithm
    
#     args
#     X: pandas.DataFrame, input vector DataFrame
#     y: pandas.DataFrame, feature vector dataframe
#     n_sample: int, number of newly generated sample
    
#     return
#     new_X: pandas.DataFrame, augmented feature vector data
#     target: pandas.DataFrame, augmented target vector data
#     """
#     indices2 = nearest_neighbour(X)
#     n = len(indices2)
#     new_X = np.zeros((n_sample, X.shape[1]))
#     target = np.zeros((n_sample, y.shape[1]))
#     for i in range(n_sample):
#         reference = random.randint(0,n-1)
#         neighbour = random.choice(indices2[reference,1:])
#         all_point = indices2[reference]
#         nn_df = y[y.index.isin(all_point)]
#         ser = nn_df.sum(axis = 0, skipna = True)
#         target[i] = np.array([1 if val>2 else 0 for val in ser])
#         ratio = random.random()
#         gap = X.loc[reference,:] - X.loc[neighbour,:]
#         new_X[i] = np.array(X.loc[reference,:] + ratio * gap)
#     new_X = pd.DataFrame(new_X, columns=X.columns)
#     target = pd.DataFrame(target, columns=y.columns)
#     new_X = pd.concat([X, new_X], axis=0)
#     target = pd.concat([y, target], axis=0)
#     return new_X, target


@app.route('/database/process', methods=['POST'])
def processDatabase():
    try:
        print('Starting process...')
        print('Cleaning session...')
        K.clear_session()


        # TO REMOVE...

        # # pd.set_option('display.max_rows', None)
        # # pd.set_option('display.max_columns', None)

        # ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
        # query_for_pre_processing = os.path.join(ROOT_DIR, 'sql_scripts', 'query_for_pre_processing.sql')
        # engine = create_engine(os.environ.get('DATABASE_URL'))
        # with engine.connect() as con:
        #     with open(query_for_pre_processing) as file:
        #         query = text(file.read())
        #         # result = con.execute(query)
        #         df = pd.read_sql(query, con = con)

        # print('Dataset sucessfuly read from db. Initiating pre-process...') 
        # # df.to_csv('D:/df_from_db.csv')
        # df.columns=['Constituent', 'Emergent Behavior']

        # compose_dataset = pd.DataFrame()
        # # print('Checkpoint! 1')
        # uniqueValues = df['Emergent Behavior'].unique()

        # for i in range (len(uniqueValues)):
        #     constituents = df[df['Emergent Behavior'] == uniqueValues[i]][['Constituent']]
        #     constituents_uniqueValues = pd.DataFrame(constituents['Constituent'].unique())
        #     constituents_Transposed = constituents_uniqueValues.T
        #     constituents_Transposed.insert(0, 'Emergent Behavior', uniqueValues[i])
        #     compose_dataset = pd.concat([compose_dataset, constituents_Transposed], ignore_index=False, axis=0)

        # #constituents_Transposed = constituents_Transposed.reset_index()
        # #del constituents_Transposed['index']

        # compose_dataset = compose_dataset.reset_index(drop=True)
        # final_dataset = compose_dataset.replace(np.nan, '')
        
        # constituents_aggregate_list = []
        # constituents_iterate_list = []
        # # print('Checkpoint! 2')
        # for i in range (len(final_dataset)):
        #     for j in range (0, len(final_dataset.columns) - 1):
        #         if (final_dataset.iloc[i][j] != ''):
        #             constituents_iterate_list.append(final_dataset.iloc[i][j])
        #     constituents_aggregate_list.append(constituents_iterate_list)
        #     constituents_iterate_list = []

        # df_constituents_aggregate_list = pd.DataFrame([constituents_aggregate_list])
        # df_constituents_aggregate_list_transposed = df_constituents_aggregate_list.T

        # emergent_behaviors_column = pd.DataFrame(final_dataset['Emergent Behavior'])

        # base_dataset = pd.concat([df_constituents_aggregate_list_transposed, emergent_behaviors_column], axis=1)
        # emergent_behaviors_column_transposed = emergent_behaviors_column.T

        # unique_sets = [list(x) for x in set(tuple(x) for x in constituents_aggregate_list)]
        # df_unique_sets = pd.DataFrame([unique_sets])
        # df_unique_sets_transposed = df_unique_sets.T
        # df_unique_sets_transposed.rename(columns={0: 'Constituents'}, inplace=True)

        # deep_learning_base_dataset = pd.DataFrame(np.zeros((len(df_unique_sets_transposed), len(emergent_behaviors_column_transposed.columns))))
        # working_deep_learning_base_dataset = deep_learning_base_dataset


        # deep_learning_base_dataset.columns = base_dataset['Emergent Behavior']

        # deep_learning_base_dataset = deep_learning_base_dataset.set_index(df_unique_sets_transposed['Constituents'])
        
        # for i in range (len(deep_learning_base_dataset)):
        #     # print('Checkpoint! 3')
        #     filter_ = base_dataset[base_dataset[0].isin([deep_learning_base_dataset.index[i]])]
        #     # print('Checkpoint! 4')
        #     filter_array = filter_['Emergent Behavior'].to_numpy()
        #     #print(filter_array)
        #     for j in range (len(deep_learning_base_dataset.columns)):
        #         for k in range (len(filter_array)):
        #             if (filter_array[k] == deep_learning_base_dataset.columns[j]):
        #                 #print('vou mudar valor')
        #                 working_deep_learning_base_dataset.iloc[i][j] = 1
        #             else:
        #                 continue               
        
        # working_deep_learning_base_dataset.insert(0, 'Constituents', df_unique_sets_transposed['Constituents'])

        # print('Dataset pre-processed sucessfuly.')
        # # print(type(working_deep_learning_base_dataset))
        # # print(working_deep_learning_base_dataset)
        # # working_deep_learning_base_dataset.to_csv('D:/working_deep_learning_base_dataset.csv')
        # print('Starting main process...')
        
        # df = pd.DataFrame(working_deep_learning_base_dataset['Constituents'].map(str))
        # # print('Checkpoint 0a...')
        # constituents = pd.DataFrame(df['Constituents'].str.split(',', expand=True).values)
        # # print('Checkpoint 0aa...')
        # # print(constituents[0]) 
        # constituents_one_hot_encoding = pd.get_dummies(constituents, prefix="Constituents")
        # # print(constituents_one_hot_encoding)
        # # print('Checkpoint 0aaa...')
        # emergent_behaviors = working_deep_learning_base_dataset.drop('Constituents', axis=1)
        # # print('Checkpoint 0b...')
        # X = constituents_one_hot_encoding
        # y = emergent_behaviors


        # output_columns_binary = []
        # # print('Checkpoint 0c...')
        # for col_name in emergent_behaviors.columns: 
        #     #print(col_name)
        #     output_columns_binary.append(col_name)
        
        # # print('SHAPE X => ', X.shape)
        # # print('LENGTH Y => ', len(y))

        # X_sub, y_sub = get_minority_instace(X, y)
        # X_res, y_res =MLSMOTE(X_sub, y_sub, 6 * len(y))
        # X_res = X_res.round(decimals = 0)
        # X_res[X_res > 1] = 1

        # X_res.columns = X_res.columns.str.replace("\[","")
        # X_res.columns = X_res.columns.str.replace("\]","")
        # X_res.columns = X_res.columns.str.replace("Constituents_","")

        # # print(X_res)

        # # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 42)
        # X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.20, random_state = 42)
        
        # dimension = np.shape(X_train)[1]
        # # print(dimension)

        # # print(np.shape(X_train))
        # # print('Checkpoint 1...')
        # main_input = Input(shape=(dimension,))
        # x = Dropout(0.3)(main_input)
        # x = Dense(10, activation='relu')(x)
        # # x = Dense(20, activation='relu')(x)
        # x = Dense(10, activation='relu')(x)
        # x = Dropout(0.3)(x)    
        
        # output_array = [] 
        # metrics_array = {}
        # loss_array = {}
        # # callbacks_array = {}
        # # print('Checkpoint 1a...')
        # for i, dense_layer in enumerate(output_columns_binary):
        #     name = f'binary_output_{i}' 
        #     # A Dense Layer is created for each output
        #     binary_output = Dense(1, activation='sigmoid', name=name)(x)
        #     output_array.append(binary_output)
        #     metrics_array[name] = 'binary_accuracy'
        #     loss_array[name] = 'binary_crossentropy'
        # # print('Checkpoint 1b...')
        # model = Model(inputs=main_input, outputs=output_array)        
        # # print('Checkpoint 2...')
        # y_train_output = []
        # for col in output_columns_binary:
        #     y_train_output.append(y_train[col])

        # zeros = (constituents_one_hot_encoding == 0).sum().sum() + (emergent_behaviors == 0).sum().sum()
        # ones = (constituents_one_hot_encoding == 1).sum().sum() + (emergent_behaviors == 1).sum().sum()
        # # print('Checkpoint 3...')
        # model.compile(optimizer='adadelta',
        #         loss=loss_array,
        #         metrics=metrics_array)   

        # if (zeros > ones):
        #     weight_binary = {0: (ones/ones), 1: (zeros/ones).round(decimals = 0)} #weighted values of zeros and ones
        # else:
        #     weight_binary = {0: (ones/zeros).round(decimals = 0), 1: (zeros/zeros)} #weighted values of zeros and ones

        # classes_weights = {}
        # for i, dense_layer in enumerate(output_columns_binary):
        #     name = f'binary_output_{i}'
        #     classes_weights[name] = weight_binary
        # # print('Checkpoint 4...')
        # # classes_weights = dict(enumerate(classes_weights))

        # # print('going to run history')

        # # print(np.shape(X_train))
        # # print(np.shape(y_train_output))

        # # history = model.fit(X_train, y_train_output, epochs=1, batch_size=8, class_weight=classes_weights, verbose=1)
        # history = model.fit(X_train, y_train_output, validation_split=0.3, epochs=50, batch_size=80, class_weight=classes_weights, verbose=1)
        
        # # print('ran history')

        # # print(history)



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

        # pca = PCA().fit(X)
        # plt.plot(np.cumsum(pca.explained_variance_ratio_))
        # plt.xlabel('number of components')
        # plt.ylabel('cumulative explained variance')

        pca = SparsePCA(n_components=10)
        pca.fit(X)
        X_pca = pca.transform(X)

        print("original shape:   ", X.shape)
        print("transformed shape:", X_pca.shape)

        xtrain, xtest, ytrain, ytest = train_test_split(X_pca, y, train_size=0.8, random_state=42)

        print('Lengths of the sets: ', len(xtrain), len(xtest), len(ytrain), len(ytest))



        token = request.json['token']
        data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
        # print('data => ', data)
        user = User.User.query.filter_by(email=data['sub']).first()
        logged_user = user.email

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


























        # # model_path = os.path.join(ROOT_DIR, 'shared', 'models', 'model_%s.h5' % ts)
        # # labels_path = os.path.join(ROOT_DIR, 'shared', 'labels', 'labels_%s.csv' % ts)
        
        # # model.save(model_path)
        # # np.savetxt(labels_path, output_columns_binary, delimiter=";", fmt='%s')

        # # print('SUCCESS!!!')

        # y_pred = model.predict(X_test)

        # THRESHOLD = 0.5

        # # report_path = pathlib.Path(os.path.join(ROOT_DIR, 'shared', 'classification_reports', ts))
        # # report_path.mkdir(parents=True, exist_ok=True)

        # f1_score_results = []
        # df_report_labels = pd.DataFrame()

        # # Binary Outputs
        # for col_idx, col in enumerate(output_columns_binary):
        #     # print(f'{col} accuracy \n')

        #     new_row = pd.DataFrame({'Index': '{:03}'.format(col_idx), 'Emergent Behavior': col}, index=[0])
        #     df_report_labels = pd.concat([df_report_labels.loc[:], new_row]).reset_index(drop=True)

        #     # Transform array of probabilities to class: 0 or 1
        #     y_pred[col_idx][y_pred[col_idx]>=THRESHOLD] = 1
        #     y_pred[col_idx][y_pred[col_idx]<THRESHOLD] = 0
        #     f1_score_results.append(f1_score(y_test[col], y_pred[col_idx], average='macro'))
        #     # print('col_idx => ', f1_score(y_test[col], y_pred[col_idx], average='macro'))
        #     # print(classification_report(y_test[col], y_pred[col_idx]))

        #     report = classification_report(y_test[col], y_pred[col_idx], output_dict=True)
        #     report.update({"accuracy": {"precision": None, "recall": None, "f1-score": report["accuracy"], "support": report['macro avg']['support']}})
              
        #     df = pd.DataFrame(report).transpose()

        #     report_filepath = os.path.join(report_path, 'report_{:03}.csv'.format(col_idx))
        #     # print('saving report: ', report_filepath)
        #     df.to_csv(report_filepath)

        # report_labels_filepath = os.path.join(report_path, 'summary.csv')
        # df_report_labels.to_csv(report_labels_filepath)

        # user_file = os.path.join(report_path, 'user.txt')
        # with open(user_file, 'w') as f:
        #     f.write(logged_user)

        # print('Total :', np.sum(f1_score_results))

        # print('f1_score_results => ', f1_score_results)
        
        # f, axes = plt.subplots(19, 2, figsize=(10,100))
        # axes = axes.ravel()

















        

        # for col_idx, col in enumerate(output_columns_binary):
        #     y_real = y_test[col]
        #     y_predito = y_pred[col_idx]

        #     # print(col_idx)
        #     # print('y_real: ', y_real, 'y_predito: ', y_predito)
        #     # print('---------------------------------------------------------------------')

        #     confusion_matrix1 = confusion_matrix(y_real, y_predito)
        #     display = ConfusionMatrixDisplay(confusion_matrix1).plot()
        #     plt.title(col)

        #     file_path = os.path.join(fig_path, 'matrix_{:03}.png'.format(col_idx))
        #     # print('saving plot: ', file_path)

        #     plt.savefig(file_path, bbox_inches='tight')
        #     plt.close()

        #     new_row = pd.DataFrame({'Index': '{:03}'.format(col_idx), 'Emergent Behavior': col}, index=[0])
        #     df_plot_labels = pd.concat([df_plot_labels.loc[:], new_row]).reset_index(drop=True)









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
        print('Starting process...')
        print('Cleaning session...')
        K.clear_session()

        # pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)

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

        # pca = PCA().fit(X)
        # plt.plot(np.cumsum(pca.explained_variance_ratio_))
        # plt.xlabel('number of components')
        # plt.ylabel('cumulative explained variance')

        pca = SparsePCA(n_components=10)
        pca.fit(X)
        X_pca = pca.transform(X)

        print("original shape:   ", X.shape)
        print("transformed shape:", X_pca.shape)

        xtrain, xtest, ytrain, ytest = train_test_split(X_pca, y, train_size=0.8, random_state=42)

        print('Lengths of the sets: ', len(xtrain), len(xtest), len(ytrain), len(ytest))

        # output_columns_binary = []
        dict_dataframes = {}
        errors = 0
        array_models = []

        # print('Checkpoint 0c...')
        for col_name in ytrain.columns: 
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
                # print('ERROR AT ', col_name)
                # print(e)
                # print()
                continue

        print('ERRORS (BEHAVIORS THAT DID NOT ANY SAMPLES FROM ONE OF THE CLASSES (MAYBE CLASS "1")): ', errors)
        print()

        new_SoS = np.zeros(len(X.columns))
        newSoS_DF = pd.DataFrame(new_SoS).T
        newSoS_DF.columns = X.columns

        constituents_elements = list(request.json['constituent_list'])

        # aux = constituents_elements[1:-1]
        # arr_constituent = aux.split(sep=',')
        # constituent_list = np.array(arr_constituent)

        # print(list(constituents_one_hot_encoding.columns))
        # print()
        # print(constituents_elements)
        # print()
        # print(type(constituents_elements))
        # print()
        # for i in range(len(constituents_elements)):
        #     # print('constituents_name => ', constituents_elements[i]['constituent_name'])
        # # print('newSoS_DF => ', newSoS_DF)
        # print()

        for i in range(len(constituents_elements)):
            constituent = constituents_elements[i]['constituent_name']
            newSoS_DF.loc[0 , constituent] = 1
            # index = list(newSoS_DF.columns).index('%s' % constituent_element['constituent_name'])
            # print('index => ', index)
            # newSoS_DF.iloc[index][0] = 1       

        # print('newSoS_DF => ', newSoS_DF)
        # print()
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
                # array_predictions.append(value)
                # print(value)

        # print(len(array_predictions))

        # predictions_DF = pd.DataFrame(array_predictions).T
        # predictions_DF.columns = y.columns

        # predicted_behaviors = predictions_DF.apply(lambda row: row[row == 1].index, axis=1)
        # array_predicted_behaviors = []

        # for i in range(len(predicted_behaviors[0])):
        #     # print(list(predicted_behaviors)[0][i])
        #     array_predicted_behaviors.append(list(predicted_behaviors)[0][i])


        print('array_predictions => ', array_predictions)
        print()

        print('array_predicted_behaviors => ', array_predicted_behaviors)
        print()




        # TO REMOVE...


        # df.columns=['Constituent', 'Emergent Behavior']

        # compose_dataset = pd.DataFrame()
        # # print('Checkpoint! 1')
        # uniqueValues = df['Emergent Behavior'].unique()

        # for i in range (len(uniqueValues)):
        #     constituents = df[df['Emergent Behavior'] == uniqueValues[i]][['Constituent']]
        #     constituents_uniqueValues = pd.DataFrame(constituents['Constituent'].unique())
        #     constituents_Transposed = constituents_uniqueValues.T
        #     constituents_Transposed.insert(0, 'Emergent Behavior', uniqueValues[i])
        #     compose_dataset = pd.concat([compose_dataset, constituents_Transposed], ignore_index=False, axis=0)

        # #constituents_Transposed = constituents_Transposed.reset_index()
        # #del constituents_Transposed['index']

        # compose_dataset = compose_dataset.reset_index(drop=True)
        # final_dataset = compose_dataset.replace(np.nan, '')
        
        # constituents_aggregate_list = []
        # constituents_iterate_list = []
        # # print('Checkpoint! 2')
        # for i in range (len(final_dataset)):
        #     for j in range (0, len(final_dataset.columns) - 1):
        #         if (final_dataset.iloc[i][j] != ''):
        #             constituents_iterate_list.append(final_dataset.iloc[i][j])
        #     constituents_aggregate_list.append(constituents_iterate_list)
        #     constituents_iterate_list = []

        # df_constituents_aggregate_list = pd.DataFrame([constituents_aggregate_list])
        # df_constituents_aggregate_list_transposed = df_constituents_aggregate_list.T

        # emergent_behaviors_column = pd.DataFrame(final_dataset['Emergent Behavior'])

        # base_dataset = pd.concat([df_constituents_aggregate_list_transposed, emergent_behaviors_column], axis=1)
        # emergent_behaviors_column_transposed = emergent_behaviors_column.T

        # unique_sets = [list(x) for x in set(tuple(x) for x in constituents_aggregate_list)]
        # df_unique_sets = pd.DataFrame([unique_sets])
        # df_unique_sets_transposed = df_unique_sets.T
        # df_unique_sets_transposed.rename(columns={0: 'Constituents'}, inplace=True)

        # deep_learning_base_dataset = pd.DataFrame(np.zeros((len(df_unique_sets_transposed), len(emergent_behaviors_column_transposed.columns))))
        # working_deep_learning_base_dataset = deep_learning_base_dataset


        # deep_learning_base_dataset.columns = base_dataset['Emergent Behavior']

        # deep_learning_base_dataset = deep_learning_base_dataset.set_index(df_unique_sets_transposed['Constituents'])
        
        # for i in range (len(deep_learning_base_dataset)):
        #     # print('Checkpoint! 3')
        #     filter_ = base_dataset[base_dataset[0].isin([deep_learning_base_dataset.index[i]])]
        #     # print('Checkpoint! 4')
        #     filter_array = filter_['Emergent Behavior'].to_numpy()
        #     #print(filter_array)
        #     for j in range (len(deep_learning_base_dataset.columns)):
        #         for k in range (len(filter_array)):
        #             if (filter_array[k] == deep_learning_base_dataset.columns[j]):
        #                 #print('vou mudar valor')
        #                 working_deep_learning_base_dataset.iloc[i][j] = 1
        #             else:
        #                 continue               
        
        # working_deep_learning_base_dataset.insert(0, 'Constituents', df_unique_sets_transposed['Constituents'])

        # print('Dataset pre-processed sucessfuly.')
        # # print(type(working_deep_learning_base_dataset))
        # # print(working_deep_learning_base_dataset)

        # print('Starting main process...')
        
        # df = pd.DataFrame(working_deep_learning_base_dataset['Constituents'].map(str))
        # # print('Checkpoint 0a...')
        # constituents = pd.DataFrame(df['Constituents'].str.split(',', expand=True).values)
        # # print('Checkpoint 0aa...')
        # # print(constituents[0]) 
        # constituents_one_hot_encoding = pd.get_dummies(constituents, prefix="Constituents")
        # # print(constituents_one_hot_encoding)
        # # print('Checkpoint 0aaa...')
        # emergent_behaviors = working_deep_learning_base_dataset.drop('Constituents', axis=1)

        # constituents_labels_replacements = {"\[":"", "\]":"", "Constituents_":"", " \'":"", "\'":""}
        # # constituents_one_hot_encoding.columns = constituents_one_hot_encoding.columns.str.replace("\[","")
        # # constituents_one_hot_encoding.columns = constituents_one_hot_encoding.columns.str.replace("\]","")
        # # constituents_one_hot_encoding.columns = constituents_one_hot_encoding.columns.str.replace("Constituents_","")

        # for (x, y) in constituents_labels_replacements.items():
        #     constituents_one_hot_encoding.columns = constituents_one_hot_encoding.columns.str.replace(x, y)
        
        # # print(constituents_one_hot_encoding)
        # # print(np.shape(constituents_one_hot_encoding)[1])

        # ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
        # model_path = os.path.join(ROOT_DIR, 'shared', 'models')

        # models_list_original = []
        # for filename in os.listdir(model_path):
        #     models_list_original.append(filename)

        # models_list_ts = []
        # string_replacements = {'model_':'', '.h5':'', '_':':',}
        # for filename in models_list_original:
        #     for (x, y) in string_replacements.items():
        #         filename = filename.replace(x, y)
        #     format_date = datetime.datetime.strptime(filename, '%Y-%m-%dT%H:%M:%S.%f')
        #     models_list_ts.append(format_date)

        # index_latest = np.argmax(models_list_ts)
        # print(models_list_original[index_latest])

        # latest_model = os.path.join(ROOT_DIR, 'shared', 'models', models_list_original[index_latest])

        # model = load_model(filepath=latest_model)
        
        # emergent_behaviors_labels = emergent_behaviors.columns.values.tolist()

        # new_SoS = np.zeros(np.shape(constituents_one_hot_encoding)[1])

        # constituents_elements=request.json['constituent_list']

        # # aux = constituents_elements[1:-1]
        # # arr_constituent = aux.split(sep=',')
        # # constituent_list = np.array(arr_constituent)

        # # print(list(constituents_one_hot_encoding.columns))

        # for constituent_element in constituents_elements:
        #     index = list(constituents_one_hot_encoding.columns).index('%s' % constituent_element['constituent_name'])
        #     new_SoS[index] = 1

        # print(new_SoS)

        # row = new_SoS
        # newX = asarray([row])
        # yhat = model.predict(newX)

        # flat_list = []
        # for sublist in yhat:
        #     for item in sublist:
        #         for subitem in item:
        #             flat_list.append(subitem)

        # # print('FLAT LIST => ', flat_list)
        # # rounded_flat_list = []

        # # for i in range(len(flat_list)):
        # #     rounded_flat_list.append(flat_list[i].round())

        # possible_emergent_behaviors = []
        # possible_emergent_behaviors_labels = []

        # for i in range(len(flat_list)):
        #     rounded_probability = flat_list[i].round()
        #     if (rounded_probability == 1):
        #         possible_emergent_behavior = {
        #             "label": emergent_behaviors_labels[i],
        #             "probability": float("{:.2f}".format(flat_list[i] * 100))
        #         }
        #         possible_emergent_behaviors.append(possible_emergent_behavior)
        #         possible_emergent_behaviors_labels.append(emergent_behaviors_labels[i])








        # emergent_behaviors_obj = Emergent_Behavior.Emergent_Behavior.query.filter(Emergent_Behavior.Emergent_Behavior.description.in_(array_predicted_behaviors))
        arr_prediction_obj = []
        # for behavior_obj in emergent_behaviors_obj:
        #     item = [p for p in array_predictions if p["behavior"] == behavior_obj.description]
        #     # probability = item[0]['probability']
        #     # probability = 1
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