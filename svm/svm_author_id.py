#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
import numpy as np


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# parse our training sets into np arrays
X = np.array(features_train[:len(features_train)])
Y = np.array(labels_train[:len(features_train)])

# create our new support vector machine classifier & set the parameters for the classifier (Kernel, gamma, and C)
#   Kernel - defines the type of classification (linear, rbf, etc)
#   gamma - determines how far we should consider values away from the decision surface. Low = far, high = close
#   C - the level to which we attempt to fit to every data point. Low = smooth line & not worried about outliers as much, high = worried about outliers and exact classification
clf = svm.SVC(C=10000, kernel='rbf')

# start a timer
t0 = time()
# train the classifier
clf.fit(X, Y)
# print time taken (for funzies)
print "training time:", round(time()-t0, 3), "s"

# start a timer
t1 = time()
# determine the accuracy
accuracy = clf.score(features_test, labels_test)
# print time taken (for funzies)
print "scoring time:", round(time()-t1, 3), "s"

# start a timer
t2 = time()
# predict who wrote each test email
pred = clf.predict(features_test)
print "prediction time:", round(time()-t2, 3), "s"

# print the predicitons for 3 random elements
print "Element 10 is ", if pred[10] == 1 then "Chris" else "Sara"
print "lement 26 is ", if pred[26] == 1 then "Chris" else "Sara"
print "lement 50 is ", if pred[50] == 1 then "Chris" else "Sara"

# get the total number of emails for each person
chrisEmails = np.count_nonzero(pred)
saraEmails = len(pred) - chrisEmails
# and print those values
print "Number of Chris emails predicted: ", chrisEmails
print "Number of Sara emails predicted: ", saraEmails

# then print our accuracy
print "score: ", accuracy