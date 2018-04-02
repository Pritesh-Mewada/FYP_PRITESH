from pymongo import MongoClient;
import pandas as pd
import numpy as np
from PreProcessingFinal import SplitByDotIp
import matplotlib.pyplot as plt
import hashlib as hb

mongoClient = MongoClient();
db = mongoClient.Cyber



def Processing(string):
    integer =  map(int,list(str(bin(int(hb.sha1(string).hexdigest(),16))[2:])))
    while len(integer)<160:
        integer.append(0)
    return integer
    

successData=[]
successOutput=[]
failedData=[]
failedOutput=[]

success = db.cowrie.find({"eventid":"cowrie.login.success"},{"username":1,"password":1,"_id":0})
failed = db.cowrie.find({"eventid":"cowrie.login.failed"},{"username":1,"password":1,"_id":0})


for i in range(0,1000):
    successData.append(Processing(success[i]['password']+success[i]['username']))
    successOutput.append(1)
       
for i in range(0,1000):
    failedData.append(Processing(failed[i]['password']+failed[i]['username']))
    failedOutput.append(0)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 160, init = 'uniform', activation = 'relu', input_dim = 160))

# Adding the second hidden layer
classifier.add(Dense(output_dim =80 , init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 80, init = 'uniform', activation = 'sigmoid'))
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))
# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 10)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)