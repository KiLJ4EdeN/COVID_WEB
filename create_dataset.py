# for this to work download the dataset from the provided link.
# then cd in the Images_Processed directory.

import os
import numpy as np
import cv2
from scipy.io import savemat

C = np.ones((349,))
N = np.zeros((397,))
labels = np.concatenate((C, N), axis=0)
covid = os.listdir('CT_COVID')
n_covid = os.listdir('CT_NonCOVID')
data=[]
for img_path in covid:
  img = cv2.imread('CT_COVID/'+img_path, cv2.IMREAD_COLOR)
  data.append(cv2.resize(img, (224, 224)))
  

for img_path in n_covid:
  img = cv2.imread('CT_NonCOVID/'+img_path, cv2.IMREAD_COLOR)
  data.append(cv2.resize(img, (224, 224)))
  
data = np.array(data)/255.
print(data.shape)
print(labels.shape)

savemat('images.mat', {'data': data,
                         'labels': labels})
