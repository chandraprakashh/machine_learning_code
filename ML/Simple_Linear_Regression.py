#Importing Libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('student_scores.csv')  

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)

# Check for outlier values
plt.boxplot(dataset.values)

#prepare the data to train the model
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 

"""
train the model now 
"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

user = float(input("Enter any numerical value only : "))
user = np.array(user).reshape(1,1)

print (regressor.predict(user))

###################################################################################

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 


"""
This means that for every one unit of change in hours studied, 
the change in the score is about 9.91%. 
"""

#making predictions
#To make pre-dictions on the test data, execute the following script:

labels_pred = regressor.predict(features_test) 

#To compare the actual output values for features_test with the predicted values, execute the following script 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  

print (df) 