#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


import numpy as np
X = np.array(features_train)
Y = np.array(labels_train)
from sklearn.naive_bayes import GaussianNB

# create our classifier
clf = GaussianNB()

# start a timer
t0 = time()
# fit (train) our classifier
clf.fit(X, Y)
# print time taken (for funzies)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
# determine the accuracy of our classifier using our real world emails and their actual associating creators
accuracy = clf.score(features_test, labels_test)
print "scoring time:", round(time()-t1, 3), "s"

t2 = time()
# predict who wrote each test email
pred = clf.predict(features_test)
print "prediction time:", round(time()-t2, 3), "s"

print accuracy
