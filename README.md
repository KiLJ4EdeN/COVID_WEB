# COVID_WEB

Create an accurate chest-ct COVID detection service and make it publicly available in a few lines of code.

Source codes for the paper: 
A Novel and Reliable Deep Learning Web-Based Tool to Detect COVID-19 Infection from Chest CT-Scan
The paper Achieved up to 90% accuracy on a dataset of about 750 CT images.
Please kindly cite the article at https://arxiv.org/abs/2006.14419, if you find this useful to your application.

NOTE: The Code is Changed to Match the Updated COVID-CT repository, if new images are modified the accuracy might have a +-1 variance.

You are free to change the code to use your desired models.

[![License](https://img.shields.io/github/license/KiLJ4EdeN/Realtime_FacialRecognition)](https://img.shields.io/github/license/KiLJ4EdeN/COVID_WEB) [![Version](https://img.shields.io/github/v/tag/KiLJ4EdeN/COVID_WEB)](https://img.shields.io/github/v/tag/KiLJ4EdeN/COVID_WEB) [![Code size](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/COVID_WEB)](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/COVID_WEB) [![Repo size](https://img.shields.io/github/repo-size/KiLJ4EdeN/COVID_WEB)](https://img.shields.io/github/repo-size/KiLJ4EdeN/COVID_WEB) [![Issue open](https://img.shields.io/github/issues/KiLJ4EdeN/COVID_WEB)](https://img.shields.io/github/issues/KiLJ4EdeN/COVID_WEB)
![Issue closed](https://img.shields.io/github/issues-closed/KiLJ4EdeN/COVID_WEB)

# Run the service right now:

* [Notebook Version](https://github.com/KiLJ4EdeN/COVID_WEB/blob/master/notebook_service.ipynb)


# Usage:
## Install Dependencies w pip:

```bash
pip3 install tensorflow sklearn opencv-contrib-python flask flask-ngrok pil numpy scipy
```

## Do this steps in order. This includes loading the data, extracting feature maps and running the service.
Remember to include the dataset in the directory.

```bash
git clone https://github.com/KiLJ4EdeN/COVID_WEB
git clone https://github.com/UCSD-AI4H/COVID-CT
cp COVID-CT/Images-processed/{CT_COVID.zip,CT_NonCOVID.zip} COVID_WEB
rm -rf COVID-CT
cd COVID_WEB
unzip CT_COVID.zip
unzip CT_NonCOVID.zip
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


Citation:

@article{Saeedi2020ANA,
  title={A Novel and Reliable Deep Learning Web-Based Tool to Detect COVID-19 Infection from Chest CT-Scan},
  author={Abdolkarim Saeedi and Maryam Saeedi and Arash Maghsoudi},
  journal={ArXiv},
  year={2020},
  volume={abs/2006.14419}
}
