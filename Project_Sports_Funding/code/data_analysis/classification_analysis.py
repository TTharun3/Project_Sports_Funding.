#%%
import pandas as pd
import numpy as np
import os
import re
import time
import json
import matplotlib.pyplot as plt
#Neural Network
import sklearn
from sklearn import metrics
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix
from sklearn import preprocessing

#%%
wd = os.getcwd()
try:
    wd = wd.replace("/code/data_analysis", "")
except: 
    pass
os.chdir(wd)
#%%
# Load train and test data into 2 dataframs
# Map the text "Story_Original" data into both of these dataframes

train_df = pd.read_csv("{}/data/data_analysis/final_data_train.csv".format(os.getcwd()))
test_df = pd.read_csv("{}/data/data_analysis/final_data_test.csv".format(os.getcwd()))
original_df = pd.read_csv("{}/data/clean_data/final_dataset_textanalysis_sentiment_score_updated.csv".format(os.getcwd()))

pd.read_csv("{}/data/clean_data/final_dataset_textanalysis_sentiment_score.csv".format(os.getcwd()))

# train split into X_train and Y_train
# test split into X_test and Y_test

train_df= pd.merge(train_df, original_df[["CampaignURL", "Story_Original"]], on="CampaignURL", how="left")
test_df = pd.merge(test_df, original_df[["CampaignURL", "Story_Original"]], on="CampaignURL", how="left")

#%%
# Split data into training and testing

X_train, Y_train = (train_df[['Wordcount', 'NarcissismFactor', 'joy',
       'sadness', 'negative', 'positive', 'fear', 'trust','numSupporters','FundingGoalAdjusted','TeamOrAthlete']], train_df.Success )

X_test, Y_test = (test_df[['Wordcount', 'NarcissismFactor', 'joy',
       'sadness', 'negative', 'positive', 'fear', 'trust','numSupporters','FundingGoalAdjusted','TeamOrAthlete']], test_df.Success )

#%%
# one-hot encode the TeamOrAthlete column in the train and test datasets
X_train = pd.concat([X_train, pd.get_dummies(train_df['TeamOrAthlete'], prefix='TeamOrAthlete')], axis=1)
X_test = pd.concat([X_test, pd.get_dummies(test_df['TeamOrAthlete'], prefix='TeamOrAthlete')], axis=1)

# Drop the original TeamOrAthlete column from the train and test datasets
X_train.drop('TeamOrAthlete', axis=1, inplace=True)
X_test.drop('TeamOrAthlete', axis=1, inplace=True)

#%%
# Numerical data transformation
# Scaling - train, test numerical data
scaler = preprocessing.StandardScaler()
scaler.fit(X_train)

# Perform the standardization process
X_train_std = scaler.transform(X_train)
X_test_std = scaler.transform(X_test)

#%%
# AUC, accuracy, sensitivity, specificity -
# Define lists for activation functions and hidden layers
activation_funcs = ['relu', 'logistic', 'tanh']

# Different hidden layer combinations
# 1 hidden layer with 50 units and 100 units
# 2 hidden layers with 50 units in each, 50 in one layer and 100 in another, 100 units in each
# 3 hidden layers with 50 units in each, 50 in first, 100 in second, 50 in third, 100 units in each
# 4 hidden layers with 50 units in each, 100 units in each
hidden_layers = [(50, ), (100, ), (50, 50), (50, 100), (100, 100), (50, 50, 50), (50, 100, 50), (100, 100, 100), (50, 50, 50, 50), (50, 100, 100, 50), (100, 100, 100, 100)]


model_list = [str(af+"-"+str(hl)) for af in activation_funcs for hl in hidden_layers]
accuracy_models = []
auc_score_models = []
sensitivity_models = []
specificity_models = []


#%%
# Train and test the neural network for different combinations of activation functions and hidden layers
for af in activation_funcs:
    for hl in hidden_layers:
        # Train and predict using the neural network
        nnclass = MLPClassifier(activation=af, solver='adam',hidden_layer_sizes=hl)
        nnclass.fit(X_train_std, Y_train)
        Y_pred = nnclass.predict(X_test_std)
        Y_pred_prob = nnclass.predict_proba(X_test_std)[:, 1]
        
        # Compute the accuracy, AUC score, confusion matrix, sensitivity, and specificity of the model on the test set
        accuracy = accuracy_score(Y_test, Y_pred)
        auc_score = roc_auc_score(Y_test, Y_pred_prob)
        tn, fp, fn, tp = confusion_matrix(Y_test, Y_pred).ravel()
        sensitivity = tp / (tp + fn)
        specificity = tn / (tn + fp)

        # Appending the metric scores into respective lists
        accuracy_models.append(accuracy)
        auc_score_models.append(auc_score)
        sensitivity_models.append(sensitivity)
        specificity_models.append(specificity)

        # Print the accuracy, AUC score, sensitivity, and specificity of the model on the test set
        print("MLP Classifier with activation function: {} and hidden layer size: {}".format(af, hl))
        print("Test set accuracy: %0.2f" % accuracy)
        print("Test set AUC score: %0.2f" % auc_score)
        print("Test set sensitivity: %0.2f" % sensitivity)
        print("Test set specificity: %0.2f" % specificity)

#%%
# Plotting the AUC scores
fig = plt.figure(figsize=(15,20))
plt.plot(auc_score_models, model_list)
plt.xlabel("AUC Score")
plt.ylabel("Model activation function and hidden layer sizes")
plt.title("Performance of various NN models on AUC Score")
for i in range(len(auc_score_models)):
    plt.text(auc_score_models[i], model_list[i], round(auc_score_models[i],3))
plt.show()


#%%
# Plotting the accuracy scores
fig = plt.figure(figsize=(15,20))
plt.plot(accuracy_models, model_list)
plt.xlabel("Accuracy")
plt.ylabel("Model activation function and hidden layer sizes")
plt.title("Performance of various NN models on Test Accuracy")
for i in range(len(accuracy_models)):
    plt.text(accuracy_models[i], model_list[i], round(accuracy_models[i],3))
plt.show()

#%%
# Plotting the sensitivity scores
fig = plt.figure(figsize=(15,20))
plt.plot(sensitivity_models, model_list)
plt.xlabel("Sensitivity")
plt.ylabel("Model activation function and hidden layer sizes")
plt.title("Performance of various NN models on Test Sensitivty")
for i in range(len(accuracy_models)):
    plt.text(sensitivity_models[i], model_list[i], round(sensitivity_models[i],3))
plt.show()
#%%
# LSTM + GloVe vectors

model_list
# %%
