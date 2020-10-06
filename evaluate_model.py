# Import Dependencies.
from sklearn.svm import SVC, NuSVC
from sklearn.model_selection import cross_val_score, StratifiedKFold, cross_val_predict
from sklearn.metrics import confusion_matrix
import numpy as np
import time
from warnings import simplefilter
from scipy.io import loadmat

# Calculate time.
s_time = time.time()
# Load the extracted features.
FV = loadmat('features.mat')
X = FV['data']
Y = FV['labels']
Y = Y.transpose()

# Create the Classifier.
clf = NuSVC(nu=0.4, kernel='rbf', gamma=0.009876939713502824, shrinking=True, tol=0.00001,
          max_iter=176, random_state=1, class_weight='balanced', probability=True)
simplefilter(action='ignore')

# Perform Cross Validation to Measure the Performance.
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=603,)

# TODO: Probably not the most optimal way to do this.
accuracy = cross_val_score(clf, X, Y, cv=cv)
scores = cross_val_score(clf, X, Y, cv=cv, scoring='roc_auc')
recall = cross_val_score(clf, X, Y, cv=cv, scoring='recall')
precision = cross_val_score(clf, X, Y, cv=cv, scoring='precision')
f1 = (2 * recall * precision) / (precision + recall)

print(f'time: {time.time() -  s_time}')
print(f'Accuracy: {np.mean(accuracy)} + {np.std(accuracy)}')
print(f'Area Under Curve: {np.mean(scores)} + {np.std(scores)}')
print(f'Recall: {np.mean(recall)} + {np.std(recall)}')
print(f'Presicion: {np.mean(precision)} + {np.std(precision)}')
print(f'f1 score: {np.mean(f1)} + {np.std(f1)}')
