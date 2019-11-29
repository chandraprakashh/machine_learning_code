
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#DT for classfication

dataset = pd.read_csv("bill_authentication.csv")  

#data analysis

dataset.shape
dataset.head()

#Preparing the dataset

features = dataset.drop('Class', axis=1)  
labels = dataset['Class']  

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  