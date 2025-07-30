
# 🍷 Wine Grade Estimator

A **Machine Learning** project that predicts the **quality of wine** using physicochemical data. It utilizes an **ElasticNet Regression** model trained via a modular ML pipeline with **MLflow tracking**. Integration with **DagsHub** allows experiment tracking in the cloud.

---

## 🔍 Overview

- 📈 Predicts wine quality (0–10) based on 11 features.
- 🧠 Uses **ElasticNet** Regression (combination of Lasso and Ridge).
- 🔧 Tuned with key hyperparameters: `alpha` and `l1_ratio`.
- 📊 Logs metrics and models via **MLflow**.
- 🌐 Deployed via a **Flask** web interface.
- ☁️ Supports **DagsHub** integration for collaborative experiment tracking.

---

## 📌 Project Workflow

1. Update `config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml` (for `alpha`, `l1_ratio`, etc.)
4. Update the `config_entity.py` (in `src/entity/`)
5. Update `configuration_manager.py` (in `src/config/`)
6. Implement/update components (e.g., ingestion, validation, transformation, training, evaluation)
7. Update pipeline scripts (in `src/pipeline/`)
8. Update `application.py` for full pipeline execution
9. Update `app.py` for UI-based prediction

---

## 🧠 ML Model: ElasticNet

ElasticNet is a linear regression model trained with both L1 and L2 regularization.

### 📌 Hyperparameters Used:

- `alpha`: Controls regularization strength
- `l1_ratio`: Balance between L1 (Lasso) and L2 (Ridge)

These are configurable via `params.yaml`.

Example:

```yaml
ElasticNet:
  alpha: 0.5
  l1_ratio: 0.3
````

---

## 🚀 How to Run the Project

### STEP 01: Clone the Repository

```bash
git clone https://github.com/tanux22/Wine-Grade-Estimator.git
cd Wine-Grade-Estimator
```

---

### STEP 02: Set Up a Python Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate     # On Linux/macOS

# On Windows (Command Prompt)
myenv\Scripts\activate.bat

# On Windows (PowerShell)
myenv\Scripts\Activate.ps1
```

> ✅ Add the environment to `.gitignore`:

```bash
echo "myenv/" >> .gitignore
```

---

### STEP 03: Install Required Packages

```bash
pip install -r requirements.txt
```

---

### STEP 04: Run the Web Application

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) to use the prediction form.

---

## 🧪 To Run the ML Pipeline

```bash
python application.py
```

This will run all stages of the pipeline: ingestion → validation → transformation → training → evaluation.

---

## 📊 MLflow Setup

**MLflow** is used to log parameters, metrics, and models.

### 👉 To Launch MLflow Locally:

```bash
mlflow ui
```

Then go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ DagsHub Integration (Cloud MLflow)

You can use **DagsHub** to view your runs remotely.

### Step 1: Export Environment Variables

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/MLFLOW_TRACKING_USERNAME/Wine-Grade-Estimator.mlflow
export MLFLOW_TRACKING_USERNAME=your username
export MLFLOW_TRACKING_PASSWORD=your password
```

Or create a `.env` file:

```ini
MLFLOW_TRACKING_URI=ttps://dagshub.com/MLFLOW_TRACKING_USERNAME/Wine-Grade-Estimator.mlflow
MLFLOW_TRACKING_USERNAME=your username
MLFLOW_TRACKING_PASSWORD=your password
```

> Note: Make sure you don’t commit `.env` by adding it to `.gitignore`.

---

## 📁 Project Structure

```
Wine-Grade-Estimator/
├── config/                          # Configuration files
│   └── config.yaml
├── logs/                            # Log files
├── myenv/                           # Python virtual environment (add to .gitignore)
├── research/                        # Jupyter notebooks for experimentation
│   ├── data_ingestion.ipynb
│   ├── data_transformation.ipynb
│   ├── data_validation.ipynb
│   ├── model_evaluation.ipynb
│   ├── model_trainer.ipynb
│   └── trials.ipynb
├── src/                             # Core source code
│   ├── components/                  # All pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── data_validation.py
│   │   ├── model_evaluation.py
│   │   └── model_trainer.py
│   ├── config/                      # Configuration manager
│   │   └── configuration.py
│   ├── constants/                   # Constants (if needed)
│   │   └── __init__.py
│   ├── entity/                      # Data class entities
│   │   └── config_entity.py
│   ├── pipeline/                    # Orchestration pipelines
│   │   ├── data_ingestion_pipeline.py
│   │   ├── data_transformation_pipeline.py
│   │   ├── data_validation_pipeline.py
│   │   ├── model_evaluation_pipeline.py
│   │   └── model_trainer_pipeline.py
│   ├── utils/                       # Utility functions
│   │   ├── common.py
│   │   └── exception.py
│   └── prediction.py                # Prediction handler
├── static/                          # Static web assets
│   ├── assets/images/
│   │   └── hero.png
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── templates/                       # HTML templates for Flask
│   ├── index.html
│   └── results.html
├── .env                             # Environment variables (MLflow, DagsHub)
├── .gitignore                       # Files/folders to ignore in Git
├── app.py                           # Flask application
├── application.py                   # Executes full pipeline
├── Dockerfile                       # (Optional) For containerization
├── LICENSE                          # License info
├── README.md                        # Project overview
├── params.yaml                      # Model and training parameters
├── requirements.txt                 # Project dependencies
├── schema.yaml                      # Input schema definition
├── setup.py                         # Package setup
├── test.py                          # For test cases
└── winequality-data.zip             # Raw dataset (optional)


```

---

## 🧠 Features

* End-to-end ML pipeline with modular architecture
* Config-driven and reusable
* Tracks all experiments with MLflow
* Supports local and remote tracking (DagsHub)
* Beautiful responsive web UI (HTML/CSS)
* ElasticNet model with customizable hyperparameters

---

## 👨‍💻 Author

**Tanush Reddy**
🔗 [GitHub](https://github.com/tanux22)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


