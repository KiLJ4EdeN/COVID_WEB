from sklearn.model_selection import cross_val_score, StratifiedKFold
import numpy as np
from bayes_opt import BayesianOptimization
from warnings import simplefilter
from scipy.io import loadmat


FV = loadmat('features.mat')
X = FV['data']
Y = FV['labels']
def svm_evaluate(                
                NU,
                GAMMA,      
                MAX_ITER,):
    simplefilter(action='ignore')
    svm = NuSVC(nu=0.4, kernel='rbf', gamma=GAMMA, shrinking=True, tol=0.00001,
              max_iter=MAX_ITER, random_state=1, class_weight='balanced', probability=True)
    
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=603,)
    scores = cross_val_score(svm, X, Y, cv=cv)
    print(np.mean(scores))

    return np.mean(scores)
   
def bayesOpt(X, Y):
    svmBO = BayesianOptimization(svm_evaluate, {                                                
                                                'NU':  (0.4),
                                                'MAX_ITER': (140.0, 190.0),
                                                'GAMMA': (0.001, 0.01)
                                            })


    svmBO.maximize(init_points=1000, n_iter=1)

    return svmBO.max
    

params = bayesOpt(X, Y)
print(params)
