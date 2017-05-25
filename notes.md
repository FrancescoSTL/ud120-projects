ud120-notes
==============


[Naive Bayes](https://github.com/FrancescoSTL/ud120-projects/tree/master/naive_bayes)
------
Utilize *prior* and *posterior* probabilities in order to calculate the probability of any given feature appearing for each label. It is considered "naive" because it only considers the frequency at which features arise and does not look at their order.

Takeaways:
1. Easy to implement
2. Very good for large data-sets, especially text learning
3. Not good if you're interested in *phrases* rather than just words

[Support Vector Machines](https://github.com/FrancescoSTL/ud120-projects/tree/master/svm)
------
Support vector machines utilize the concept of *margin* to determine the decision boundaries for classifiers. In splitting distance (margin) between data points in the set, the SVMs can create precise classifications. They utilize these 3 main concepts:

1. Kernel - defines the type of classification (linear, rbf, etc)
2. gamma - determines how far we should consider values away from the decision surface. Low = far, high = close
3. C - the level to which we attempt to fit to every data point. Low = smooth line & not worried about outliers as much, high = worried about outliers and exact classification

Takeaways:
1. Not suited for text learning
2. Takes a relatively long time to run
3. Prone to overclassification (too detailed decision boundary), esp if given high C
