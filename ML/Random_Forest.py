#Import libraries
import pandas as pd  
import numpy as np  

#import database
dataset = pd.read_csv('petrol_consumption.csv') 

#Data Analysis
print (dataset.head())

#Preparing the data for training
features = dataset.iloc[:, 0:4].values  
labels = dataset.iloc[:, 4].values  

#Traing test split
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

#feature scaling
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  

#train the model
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  

#Evaluating the algorithm
from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred)))  

print (np.mean(labels))

"""
With 20 trees, the root mean squared error is 64.93 which is greater than 10 percent 
of the average petrol consumption i.e. 576.77. This may indicate, among other things,
that we have not used enough estimators (trees).
"""

#Change the number of estimators
regressor = RandomForestRegressor(n_estimators=300, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  

#Evaluating the algorithm with 300 trees

print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred)))