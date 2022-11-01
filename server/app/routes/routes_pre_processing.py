from app import app, db
from flask import jsonify, request
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text
from models import SoS, Constituent, Basic_Feature, Emergent_Behavior, SoS_Constituent, Constituent_Basic_Feature, Basic_Feature_Emergent_Behavior, SoS_Emergent_Behavior
import os

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
import matplotlib.pyplot as plt
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

load_dotenv()

def get_tail_label(df):
    """
    Give tail label colums of the given target dataframe
    
    args
    df: pandas.DataFrame, target label df whose tail label has to identified
    
    return
    tail_label: list, a list containing column name of all the tail label
    """
    columns = df.columns
    n = len(columns)
    irpl = np.zeros(n)
    for column in range(n):
        irpl[column] = df[columns[column]].value_counts()[1]
    irpl = max(irpl)/irpl
    mir = np.average(irpl)
    tail_label = []
    for i in range(n):
        if irpl[i] >= mir:
            tail_label.append(columns[i])
    return tail_label

def get_index(df):
  """
  give the index of all tail_label rows
  args
  df: pandas.DataFrame, target label df from which index for tail label has to identified
    
  return
  index: list, a list containing index number of all the tail label
  """
  tail_labels = get_tail_label(df)
  index = set()
  for tail_label in tail_labels:
    sub_index = set(df[df[tail_label]==1].index)
    index = index.union(sub_index)
  return list(index)

def get_minority_instace(X, y):
    """
    Give minority dataframe containing all the tail labels
    
    args
    X: pandas.DataFrame, the feature vector dataframe
    y: pandas.DataFrame, the target vector dataframe
    
    return
    X_sub: pandas.DataFrame, the feature vector minority dataframe
    y_sub: pandas.DataFrame, the target vector minority dataframe
    """
    index = get_index(y)
    X_sub = X[X.index.isin(index)].reset_index(drop = True)
    y_sub = y[y.index.isin(index)].reset_index(drop = True)
    return X_sub, y_sub

def nearest_neighbour(X):
    """
    Give index of 5 nearest neighbor of all the instance
    
    args
    X: np.array, array whose nearest neighbor has to find
    
    return
    indices: list of list, index of 5 NN of each element in X
    """
    nbs=NearestNeighbors(n_neighbors=5,metric='euclidean',algorithm='kd_tree').fit(X)
    euclidean,indices= nbs.kneighbors(X)
    return indices

def MLSMOTE(X,y, n_sample):
    """
    Give the augmented data using MLSMOTE algorithm
    
    args
    X: pandas.DataFrame, input vector DataFrame
    y: pandas.DataFrame, feature vector dataframe
    n_sample: int, number of newly generated sample
    
    return
    new_X: pandas.DataFrame, augmented feature vector data
    target: pandas.DataFrame, augmented target vector data
    """
    indices2 = nearest_neighbour(X)
    n = len(indices2)
    new_X = np.zeros((n_sample, X.shape[1]))
    target = np.zeros((n_sample, y.shape[1]))
    for i in range(n_sample):
        reference = random.randint(0,n-1)
        neighbour = random.choice(indices2[reference,1:])
        all_point = indices2[reference]
        nn_df = y[y.index.isin(all_point)]
        ser = nn_df.sum(axis = 0, skipna = True)
        target[i] = np.array([1 if val>2 else 0 for val in ser])
        ratio = random.random()
        gap = X.loc[reference,:] - X.loc[neighbour,:]
        new_X[i] = np.array(X.loc[reference,:] + ratio * gap)
    new_X = pd.DataFrame(new_X, columns=X.columns)
    target = pd.DataFrame(target, columns=y.columns)
    new_X = pd.concat([X, new_X], axis=0)
    target = pd.concat([y, target], axis=0)
    return new_X, target


@app.route('/pre_process_database')
def pre_process_database():
    try:
        print('Starting process...') 
        ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
        query_for_pre_processing = os.path.join(ROOT_DIR, 'sql_scripts', 'query_for_pre_processing.sql')
        engine = create_engine(os.environ.get('DATABASE_URL'))
        with engine.connect() as con:
            with open(query_for_pre_processing) as file:
                query = text(file.read())
                # result = con.execute(query)
                df = pd.read_sql(query, con = con)

        print('Dataset sucessfuly read from db. Initiating pre-process...') 

        df.columns=['Constituent', 'Emergent Behavior']

        compose_dataset = pd.DataFrame()
        # print('Checkpoint! 1')
        uniqueValues = df['Emergent Behavior'].unique()

        for i in range (len(uniqueValues)):
            constituents = df[df['Emergent Behavior'] == uniqueValues[i]][['Constituent']]
            constituents_uniqueValues = pd.DataFrame(constituents['Constituent'].unique())
            constituents_Transposed = constituents_uniqueValues.T
            constituents_Transposed.insert(0, 'Emergent Behavior', uniqueValues[i])
            compose_dataset = pd.concat([compose_dataset, constituents_Transposed], ignore_index=False, axis=0)

        #constituents_Transposed = constituents_Transposed.reset_index()
        #del constituents_Transposed['index']

        compose_dataset = compose_dataset.reset_index(drop=True)
        final_dataset = compose_dataset.replace(np.nan, '')
        
        constituents_aggregate_list = []
        constituents_iterate_list = []
        # print('Checkpoint! 2')
        for i in range (len(final_dataset)):
            for j in range (0, len(final_dataset.columns) - 1):
                if (final_dataset.iloc[i][j] != ''):
                    constituents_iterate_list.append(final_dataset.iloc[i][j])
            constituents_aggregate_list.append(constituents_iterate_list)
            constituents_iterate_list = []

        df_constituents_aggregate_list = pd.DataFrame([constituents_aggregate_list])
        df_constituents_aggregate_list_transposed = df_constituents_aggregate_list.T

        emergent_behaviors_column = pd.DataFrame(final_dataset['Emergent Behavior'])

        base_dataset = pd.concat([df_constituents_aggregate_list_transposed, emergent_behaviors_column], axis=1)
        emergent_behaviors_column_transposed = emergent_behaviors_column.T

        unique_sets = [list(x) for x in set(tuple(x) for x in constituents_aggregate_list)]
        df_unique_sets = pd.DataFrame([unique_sets])
        df_unique_sets_transposed = df_unique_sets.T
        df_unique_sets_transposed.rename(columns={0: 'Constituents'}, inplace=True)

        deep_learning_base_dataset = pd.DataFrame(np.zeros((len(df_unique_sets_transposed), len(emergent_behaviors_column_transposed.columns))))
        working_deep_learning_base_dataset = deep_learning_base_dataset

        deep_learning_base_dataset.columns = base_dataset['Emergent Behavior']

        deep_learning_base_dataset = deep_learning_base_dataset.set_index(df_unique_sets_transposed['Constituents'])
        
        for i in range (len(deep_learning_base_dataset)):
            # print('Checkpoint! 3')
            filter_ = base_dataset[base_dataset[0].isin([deep_learning_base_dataset.index[i]])]
            # print('Checkpoint! 4')
            filter_array = filter_['Emergent Behavior'].to_numpy()
            #print(filter_array)
            for j in range (len(deep_learning_base_dataset.columns)):
                for k in range (len(filter_array)):
                    if (filter_array[k] == deep_learning_base_dataset.columns[j]):
                        #print('vou mudar valor')
                        working_deep_learning_base_dataset.iloc[i][j] = 1
                    else:
                        continue               
        
        working_deep_learning_base_dataset.insert(0, 'Constituents', df_unique_sets_transposed['Constituents'])

        print('Dataset pre-processed sucessfuly.')
        # print(type(working_deep_learning_base_dataset))

        print('Starting main process...')
        
        df = pd.DataFrame(working_deep_learning_base_dataset['Constituents'].map(str))
        # print('Checkpoint 0a...')
        constituents = pd.DataFrame(df['Constituents'].str.split(',', expand=True).values)
        # print('Checkpoint 0aa...')
        # print(constituents[0]) 
        constituents_one_hot_encoding = pd.get_dummies(constituents, prefix="Constituents")
        # print(constituents_one_hot_encoding)
        # print('Checkpoint 0aaa...')
        emergent_behaviors = working_deep_learning_base_dataset.drop('Constituents', axis=1)
        # print('Checkpoint 0b...')
        X = constituents_one_hot_encoding
        y = emergent_behaviors

        print(np.shape(X))

        output_columns_binary = []
        # print('Checkpoint 0c...')
        for col_name in emergent_behaviors.columns: 
            #print(col_name)
            output_columns_binary.append(col_name)
        
        X_sub, y_sub = get_minority_instace(X, y)
        X_res,y_res =MLSMOTE(X_sub, y_sub, 85)
        X_res = X_res.round(decimals = 0)

        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 42)
        X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.20, random_state = 42)
        
        # print(np.shape(X_train))
        # print('Checkpoint 1...')
        main_input = Input(shape=(65,))
        x = Dropout(0.3)(main_input)
        x = Dense(10, activation='relu')(x)
        # x = Dense(20, activation='relu')(x)
        x = Dense(10, activation='relu')(x)
        x = Dropout(0.3)(x)    
        
        output_array = [] 
        metrics_array = {}
        loss_array = {}
        # callbacks_array = {}
        # print('Checkpoint 1a...')
        for i, dense_layer in enumerate(output_columns_binary):
            name = f'binary_output_{i}' 
            # A Dense Layer is created for each output
            binary_output = Dense(1, activation='sigmoid', name=name)(x)
            output_array.append(binary_output)
            metrics_array[name] = 'binary_accuracy'
            loss_array[name] = 'binary_crossentropy'
        # print('Checkpoint 1b...')
        model = Model(inputs=main_input, outputs=output_array)        
        # print('Checkpoint 2...')
        y_train_output = []
        for col in output_columns_binary:
            y_train_output.append(y_train[col])

        weight_of_zeros = (constituents_one_hot_encoding == 0).sum().sum() + (emergent_behaviors == 0).sum().sum()
        weight_of_ones = (constituents_one_hot_encoding == 1).sum().sum() + (emergent_behaviors == 1).sum().sum()
        # print('Checkpoint 3...')
        model.compile(optimizer='adadelta',
                loss=loss_array,
                metrics=metrics_array)   

        weight_binary = {0: 1, 1: 14} #weighted values of zeros and ones
        classes_weights = {}
        for i, dense_layer in enumerate(output_columns_binary):
            name = f'binary_output_{i}'
            classes_weights[name] = weight_binary
        # print('Checkpoint 4...')
        # classes_weights = dict(enumerate(classes_weights))

        print('going to run history')

        print(np.shape(X_train))
        print(np.shape(y_train_output))

        # history = model.fit(X_train, y_train_output, epochs=1, batch_size=8, class_weight=classes_weights, verbose=1)
        history = model.fit(X_train, y_train_output, validation_split=0.3, epochs=50, batch_size=80, class_weight=classes_weights, verbose=1)
        
        print('ran history')

        print(history)

        model.save('./model.h5')

        np.savetxt("./labels.csv", output_columns_binary, delimiter=";", fmt='%s')

        print('SUCCESS!!!')
        return jsonify('OK!')  
    except Exception as e:
        # db.session.rollback()
        return(str(e))     


@app.route('/predict')
def predict():
    try:
        model = load_model(filepath="./model.h5")
        
        output_columns_binary =[]
        with open('./labels.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader: 
                output_columns_binary.append(row)
        f.close()

        behaviors = []
        for sublist in output_columns_binary:
            for item in sublist:
                behaviors.append(item)


        new_SoS = np.zeros(65)
        new_SoS[18] = 1
        new_SoS[44] = 1
        new_SoS[60] = 1

        row = new_SoS
        newX = asarray([row])
        yhat = model.predict(newX)

        flat_list = []
        for sublist in yhat:
            for item in sublist:
                for subitem in item:
                    flat_list.append(subitem)

        rounded_flat_list = []

        for i in range(len(flat_list)):
            rounded_flat_list.append(flat_list[i].round())

        possible_emergent_behaviors = []

        for i in range(len(rounded_flat_list)):
            if (rounded_flat_list[i] == 1):
                possible_emergent_behaviors.append(behaviors[i])

        return jsonify(possible_emergent_behaviors)
    except Exception as e:
        return(str(e))


def process_database(dataframe):
    try:
        print('Starting main process...')
        
        df = pd.DataFrame(dataframe['Constituents'].map(str))
        print('Checkpoint 0a...')
        constituents = pd.DataFrame(df['Constituents'].str.split(',', expand=True).values)
        print('Checkpoint 0aa...')
        # print(constituents[0]) 
        constituents_one_hot_encoding = pd.get_dummies(constituents, prefix="Constituents")
        # print(constituents_one_hot_encoding)
        print('Checkpoint 0aaa...')
        emergent_behaviors = dataframe.drop('Constituents', axis=1)
        print('Checkpoint 0b...')
        X = constituents_one_hot_encoding
        y = emergent_behaviors

        output_columns_binary = []
        print('Checkpoint 0c...')
        for col_name in emergent_behaviors.columns: 
            #print(col_name)
            output_columns_binary.append(col_name)
        
        X_sub, y_sub = get_minority_instace(X, y)
        X_res,y_res =MLSMOTE(X_sub, y_sub, 85)
        X_res = X_res.round(decimals = 0)

        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 42)
        X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.20, random_state = 42)

        print('Checkpoint 1...')
        main_input = Input(shape=(68,))
        x = Dropout(0.3)(main_input)
        x = Dense(10, activation='relu')(x)
        # x = Dense(20, activation='relu')(x)
        x = Dense(10, activation='relu')(x)
        x = Dropout(0.3)(x)    
        
        output_array = [] 
        metrics_array = {}
        loss_array = {}
        # callbacks_array = {}
        print('Checkpoint 1a...')
        for i, dense_layer in enumerate(output_columns_binary):
            name = f'binary_output_{i}' 
            # A Dense Layer is created for each output
            binary_output = Dense(1, activation='sigmoid', name=name)(x)
            output_array.append(binary_output)
            metrics_array[name] = 'binary_accuracy'
            loss_array[name] = 'binary_crossentropy'
        print('Checkpoint 1b...')
        model = Model(inputs=main_input, outputs=output_array)        
        print('Checkpoint 2...')
        y_train_output = []
        for col in output_columns_binary:
            y_train_output.append(y_train[col])

        weight_of_zeros = (constituents_one_hot_encoding == 0).sum().sum() + (emergent_behaviors == 0).sum().sum()
        weight_of_ones = (constituents_one_hot_encoding == 1).sum().sum() + (emergent_behaviors == 1).sum().sum()
        print('Checkpoint 3...')
        model.compile(optimizer='adadelta',
                loss=loss_array,
                metrics=metrics_array)   

        weight_binary = {0: 1, 1: 14} #weighted values of zeros and ones
        classes_weights = {}
        for i, dense_layer in enumerate(output_columns_binary):
            name = f'binary_output_{i}'
            classes_weights[name] = weight_binary
        print('Checkpoint 4...')
        # classes_weights = dict(enumerate(classes_weights))

        print('going to run history')

        # history = model.fit(X_train, y_train_output, epochs=1, batch_size=8, class_weight=classes_weights, verbose=1)
        history = model.fit(X_train, y_train_output, validation_split=0.3, epochs=50, batch_size=80, class_weight=classes_weights, verbose=1)
        
        print('ran history')

        print(history)

        # REVIEW FROM HERE ON...

        # hist_df = pd.DataFrame(history.history)
        # df_acurracies = hist_df.iloc[:, 38:74]
        # n = len(df_acurracies)

        # accuracy = []
        # epoch = []
        # print('Checkpoint 5...')
        # for i in range(n):
        #     epoch.append(i)
        #     accuracy.append(mean(df_acurracies.iloc[i].values))
        #     print('Epoch', i, '- Accuracy:', mean(df_acurracies.iloc[i].values))   
        # print('Checkpoint 6...')
        # # t = epoch
        # # s = accuracy

        # # fig, ax = plt.subplots()
        # # ax.plot(t, s)
        # print('Checkpoint 7...')

        # # ax.set(xlabel='Epoch', ylabel='Accuracy',
        # #     title='Evolution of Accuracy of the model through epochs')
        # # ax.grid()

        # # fig.savefig("accuracy_evolution.png")
        # # plt.show()              

        # # model.summary()
        # # plot_model(model, to_file='model_plot4a.png', show_shapes=True, show_layer_names=True)

        # # return jsonify('Database processed sucessfully!')

        # y_pred = model.predict(X_test)

        # THRESHOLD = 0.5 # threshold between classes

        # precision_results = []
        # recall_results = []
        # f1_score_results = []

        # overall_precision = []
        # overall_recall = []
        # overall_f1 = []

        # # Binary Outputs
        # for col_idx, col in enumerate(output_columns_binary):
        #     print(f'{col_idx}', '-' , f'{col}')
            
        #     # print('y_pred[col_idx]: ', y_pred[col_idx])
        #     # print('y_pred[col_idx][y_pred[col_idx]>=THRESHOLD]:', y_pred[col_idx][y_pred[col_idx]>=THRESHOLD])
        #     # print('y_pred[col_idx][y_pred[col_idx]<THRESHOLD]:', y_pred[col_idx][y_pred[col_idx]<THRESHOLD])
        #     # print('y_test[col]:', y_test[col])

        #     # Transform array of probabilities to class: 0 or 1
        #     y_pred[col_idx][y_pred[col_idx]>=THRESHOLD] = 1
        #     y_pred[col_idx][y_pred[col_idx]<THRESHOLD] = 0

        #     precision_results.append(precision_score(y_test[col], y_pred[col_idx], average='macro'))
        #     recall_results.append(recall_score(y_test[col], y_pred[col_idx], average='macro'))
        #     f1_score_results.append(f1_score(y_test[col], y_pred[col_idx], average='macro'))
            
        #     # print(classification_report(y_test[col], y_pred[col_idx]))
        #     overall_precision.append(mean(precision_results))
        #     overall_recall.append(mean(recall_results))
        #     overall_f1.append(mean(f1_score_results))
        #     print('Precision: %.2f - Recall: %.2f - F1-Score: %.2f' % (mean(precision_results), mean(recall_results), mean(f1_score_results)))
        #     print()

        # mean_precision = mean(overall_precision)
        # mean_recall = mean(overall_recall)
        # mean_f1 = mean(overall_f1)

        # print('Mean values =>>> Precision: %.3f - Recall: %.3f - F1-Score: %.3f' % (mean_precision, mean_recall, mean_f1))

        # y_pred_train = model.predict(X_train)

        # precision_results = []
        # recall_results = []
        # f1_score_results = []

        # overall_precision = []
        # overall_recall = []
        # overall_f1 = []

        # # Binary Outputs
        # for col_idx, col in enumerate(output_columns_binary):
        #     print(f'{col_idx}', '-' , f'{col}')

        #     # Transform array of probabilities to class: 0 or 1
        #     y_pred_train[col_idx][y_pred_train[col_idx]>=THRESHOLD] = 1
        #     y_pred_train[col_idx][y_pred_train[col_idx]<THRESHOLD] = 0

        #     precision_results.append(precision_score(y_train[col], y_pred_train[col_idx], average='macro'))
        #     recall_results.append(recall_score(y_train[col], y_pred_train[col_idx], average='macro'))
        #     f1_score_results.append(f1_score(y_train[col], y_pred_train[col_idx], average='macro'))
            
        #     # print(classification_report(y_test[col], y_pred[col_idx]))
        #     overall_precision.append(mean(precision_results))
        #     overall_recall.append(mean(recall_results))
        #     overall_f1.append(mean(f1_score_results))
        #     print('Precision: %.2f - Recall: %.2f - F1-Score: %.2f' % (mean(precision_results), mean(recall_results), mean(f1_score_results)))
        #     print()

        # mean_precision = mean(overall_precision)
        # mean_recall = mean(overall_recall)
        # mean_f1 = mean(overall_f1)

        # print('Mean values =>>> Precision: %.3f - Recall: %.3f - F1-Score: %.3f' % (mean_precision, mean_recall, mean_f1))    
    
        # print('Checkpoint 8...')
        
    except Exception as e:
	    return(str(e))    