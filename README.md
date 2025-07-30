# Wine-Grade-Estimator

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/tanux22/Wine-Grade-Estimator.git
```
### STEP 01- Create a python environment after opening the repository

```bash
python3 -m venv myenv
```

```bash
source myenv/bin/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/atanushreddy/Wine-Grade-Estimator.mlflow \
MLFLOW_TRACKING_USERNAME=atanushreddy \
MLFLOW_TRACKING_PASSWORD=702b03e47aedac5981cd5ae775223366bc2b1711 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/atanushreddy/Wine-Grade-Estimator.mlflow

export MLFLOW_TRACKING_USERNAME=atanushreddy 

export MLFLOW_TRACKING_PASSWORD=702b03e47aedac5981cd5ae775223366bc2b1711

```


