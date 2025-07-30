import os
from src import logger
from src.exception import CustomException
import sys
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import mlflow
from urllib.parse import urlparse
import mlflow.sklearn
import numpy as np  
import joblib
from src.utils.common import save_json
import tempfile
from src.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from dotenv import load_dotenv



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
        
    def eval_metrics(self, actual, predicted):
        """
        Calculate evaluation metrics.
        """
        r2 = r2_score(actual, predicted)
        mae = mean_absolute_error(actual, predicted)
        mse = mean_squared_error(actual, predicted)
        rmse = np.sqrt(mse)

        return rmse, mae, mse, r2

    def log_into_mlflow(self):
        """ Log evaluation metrics into MLflow.
        """
        try:
            load_dotenv()

            os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
            os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

            test_df = pd.read_csv(self.config.test_data_file_path)
            model=joblib.load(self.config.model_path)
        
            X_test = test_df.drop(columns=[self.config.target_column],axis=1)
            y_test = test_df[self.config.target_column]
        
            mlflow.set_tracking_uri(self.config.mlflow_uri)
            mlflow.set_experiment("WineGradeEvaluation")
            tracking_uri = urlparse(mlflow.get_tracking_uri()).scheme
            
            with mlflow.start_run():
                predicted_qualities = model.predict(X_test)
                rmse, mae, mse, r2 = self.eval_metrics(y_test, predicted_qualities)
                
                scores = {
                    "rmse": rmse,
                    "mae": mae,
                    "mse": mse,
                    "r2": r2
                }
                
                save_json(file_path=Path(self.config.evaluation_report), data=scores)
                
                mlflow.log_params(self.config.all_params)
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("mse", mse)
                mlflow.log_metric("r2", r2)
                
                with tempfile.TemporaryDirectory() as temp_dir:
                    model_output_path = os.path.join(temp_dir, "model")
                    os.makedirs(model_output_path, exist_ok=True)
                    joblib.dump(model, os.path.join(model_output_path, "model.pkl"))
                    mlflow.log_artifacts(model_output_path, artifact_path="model")
                
        except Exception as e:
            raise CustomException(e, sys)