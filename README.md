# COVID_WEB

Create an accurate chest-ct COVID detection service and make it publicly available in a few lines of code.

Source codes for the paper: 
A Novel and Reliable Deep Learning Web-Based Tool to Detect COVID-19 Infection from Chest CT-Scan
The paper Achieved up to 90% accuracy on a dataset of about 750 CT images.
Please kindly cite the article at https://arxiv.org/abs/2006.14419, if you find this useful to your application.

NOTE: The Code is Changed to Match the Updated COVID-CT repository, the accuracy might have a +-3 variance.

You are free to change the code to use your desired models.

[![License](https://img.shields.io/github/license/KiLJ4EdeN/Realtime_FacialRecognition)](https://img.shields.io/github/license/KiLJ4EdeN/COVID_WEB) [![Code size](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/COVID_WEB)](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/COVID_WEB) [![Repo size](https://img.shields.io/github/repo-size/KiLJ4EdeN/COVID_WEB)](https://img.shields.io/github/repo-size/KiLJ4EdeN/COVID_WEB) [![Open Issues](https://img.shields.io/github/issues/KiLJ4EdeN/COVID_WEB)](https://img.shields.io/github/issues/KiLJ4EdeN/COVID_WEB)
![Closed Issues](https://img.shields.io/github/issues-closed/KiLJ4EdeN/COVID_WEB)


## Dataset:
Full dataset is available on 

Some samples are shown below:
![](https://github.com/KiLJ4EdeN/COVID_WEB/blob/master/images/covid.jpg)



## Proposed Scheme:
![](https://github.com/KiLJ4EdeN/COVID_WEB/blob/master/images/workflow.jpg)
![](https://github.com/KiLJ4EdeN/COVID_WEB/blob/master/images/densenet.png)


## Run the service right now:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KiLJ4EdeN/COVID_WEB/blob/master/notebook_service.ipynb)

[Notebook Version](https://github.com/KiLJ4EdeN/COVID_WEB/blob/master/notebook_service.ipynb)

## Or Install on a Local Computer.

```bash
git clone https://github.com/KiLJ4EdeN/COVID_WEB
cd COVID_WEB
chmod +x server.sh
./server.sh
```

The ngrok host url should be displayed.

Note that you can comment out flask ngrok if you dont have an internet connection.

## Results:

Upload An Image:
<img src="https://github.com/KiLJ4EdeN/COVID_WEB/blob/master/images/upload.jpg" width="800" height="400" />

Get the Results:
<img src="https://github.com/KiLJ4EdeN/COVID_WEB/blob/master/images/result.jpg" width="200" height="200" />



## Additional utils
### These let you see the classification metrics, or get new parameters with bayesian optimization.
```bash
pip3 install bayesian-optimization
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
