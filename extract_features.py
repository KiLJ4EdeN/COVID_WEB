# This code performes a dimension reduction on the dataset,
# Using a DenseNet121 pretrained model.

import tensorflow as tf
from scipy.io import loadmat, savemat
import numpy as np

# Load saved preprocessed images.
FV = loadmat('images.mat')
data = FV['data']
labels = FV['labels']
labels = labels.transpose()
labels = labels.ravel()

# Create the model.
inputs = tf.keras.Input(shape=(224, 224, 3))
# Here different models were tested, 
# TODO : add all the models in parallel with the best model.
model = tf.keras.applications.DenseNet121(include_top=False, weights='imagenet',
                                          input_shape=(224,224,3))
# Possibly try other models here.
model_outputs = model(inputs)
outputs = tf.keras.layers.GlobalAveragePooling2D(name='ga')(model_outputs)
feature_extractor = tf.keras.models.Model(inputs=inputs, outputs=outputs)

# Get features in a memory friendly way.
X = []
samples = data.shape[0]
for i in range(samples):
  X.append(feature_extractor(np.array([data[i]])))
X = np.array(X)
# Replace old images with features.
data = X.reshape(746, 1024)
del X

# Save the Exctracted Features.
savemat('features.mat', {'data': data,
                         'labels': labels})
