'''

this is the data set of many peoples in which we are trying to predict the affair of a women.

'''

# K-Nearest Neighbors (K-NN)

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('affairs.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, 8].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

# finding the accuracy of training 
print("Training Accuracy: ",classifier.score(features_train,labels_train))
print("Test Accuracy: ",classifier.score(features_test,labels_test))
