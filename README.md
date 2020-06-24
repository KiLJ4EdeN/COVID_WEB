# DeepCOVID
Create an accurate chest-ct COVID detection service in a few lines of code.

You are free to change the code to use your desired models.


[![License](https://img.shields.io/github/license/KiLJ4EdeN/Realtime_FacialRecognition)](https://img.shields.io/github/license/KiLJ4EdeN/DeepCOVID) [![Version](https://img.shields.io/github/v/tag/KiLJ4EdeN/DeepCOVID)](https://img.shields.io/github/v/tag/KiLJ4EdeN/DeepCOVID) [![Code size](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/DeepCOVID)](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/DeepCOVID) [![Repo size](https://img.shields.io/github/repo-size/KiLJ4EdeN/DeepCOVID)](https://img.shields.io/github/repo-size/KiLJ4EdeN/DeepCOVID) [![Issue open](https://img.shields.io/github/issues/KiLJ4EdeN/DeepCOVID)](https://img.shields.io/github/issues/KiLJ4EdeN/DeepCOVID)
![Issue closed](https://img.shields.io/github/issues-closed/KiLJ4EdeN/DeepCOVID)


# Usage:
## Install Dependencies w pip:

1- tensorflow

2- sklearn

3- opencv-contrib-python

4- flask

5- flask-ngrok

6- pil

7- numpy

8- scipy

## Download the dataset and unzip the images:
```bash
git clone https://github.com/UCSD-AI4H/COVID-CT
cd COVID-CT/Images-processed/
unzip CT-COVID.zip
unzip CT-NonCOVID.zip
```


## Do this steps in order. This includes loading the data, extracting feature maps and running the service.

```bash
git clone https://github.com/KiLJ4EdeN/DeepCOVID
cd DeepCOVID
python3 create_dataset.py
python3 extract_features.py
python3 server.py
```
The ngrok host url should be displayed.

Note that you can comment out flask ngrok if you dont have an internet connection.


## Additional utils
### These let you see the classification metrics, or get new parameters with bayesian optimization.
```bash
python3 run_bayesian_optimization.py
python3 evaluate_model.py
```
Consider that this is just for demonstration, since the model is already using optimal parameters.
