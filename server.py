# webservice
#
# $ curl -XPOST -F "file=@covid.jpg" http://127.0.0.1:5001

from flask import Flask, jsonify, request, redirect
from flask_ngrok import run_with_ngrok
import cv2
import PIL
import numpy as np
from sklearn.svm import NuSVC
import pickle
from scipy.io import loadmat

# create svm
FV = loadmat('features.mat')
X = FV['data']
Y = FV['labels']
clf = NuSVC(nu=0.4, kernel='rbf', gamma=0.009876939713502824, shrinking=True, tol=0.00001,
          max_iter=176, random_state=1, class_weight='balanced', probability=True)
clf.fit(X, Y)
with open('svm_model.pkl', 'wb') as f:
  pickle.dump(clf, f)

# define detection and loading fn's.'
def detect(imagePath, models):
  import numpy as np
  import cv2
  import time

  s_time = time.time()
  covid19 = False
  image = imagePath
  feature_extractor, clf = models
  image = cv2.resize(image, (224, 224))
  features = feature_extractor(np.array([image]))
  features = np.array(features).reshape(1024, 1)
  pred = np.around(clf.predict(features.reshape(1, -1)))
  if pred == 1:
    covid19 = True
  return {'covid19': covid19,
          'response_time': time.time()-s_time}

def load_models():
  import tensorflow as tf
  import pickle

  inputs = tf.keras.Input(shape=(224, 224, 3))
  model = tf.keras.applications.DenseNet121(include_top=False, weights='imagenet',
                                            input_shape=(224,224,3))
  model_outputs = model(inputs)
  outputs = tf.keras.layers.GlobalAveragePooling2D(name='ga')(model_outputs)
  feature_extractor = tf.keras.models.Model(inputs=inputs, outputs=outputs)
  with open('svm_model.pkl', 'rb') as f:
    clf = pickle.load(f)
  return [feature_extractor, clf]
  
  
 
models = load_models()
# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
run_with_ngrok(app)


# define loading fn.
def load_image_file(file, mode='RGB'):
    """
    Loads an image file (.jpg, .png, etc) into a numpy array
    :param file: image file name or file object to load
    :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
    :return: image contents as numpy array
    """
    im = PIL.Image.open(file)
    if mode:
        im = im.convert(mode)
    return np.array(im)

# check for desired file extensions.
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            return detect_covid(file)

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Computerized Tomography COVID Detection.</title>
    <head>
    <style>
    body {
      background-color: gray;
    }
    </style>    
    </head>
    <h1>Upload a CT image and see if its COVID positive!</h1>
    <h2>The method gains an AUC of 95% So there is no gurantee of correct diagnosis.</h2>
    <hr>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


def detect_covid(file_stream):
    image = load_image_file(file_stream)
    result =  detect(image, models)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
