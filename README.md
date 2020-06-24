# DeepCOVID
A novel application for covid detection using a deep learning web-service.

# to use:
## do this steps in order to run the service.

```bash
git clone https://github.com/KiLJ4EdeN/DeepCOVID
cd DeepCOVID
python3 create_dataset.py
python3 extract_features.py
python3 server.py
```

## additional utils
### these let you see the classification metrics, or get new parameters with bayesian optimization.
```bash
python3 run_bayesian_optimization.py
python3 evaluate_model.py
```
