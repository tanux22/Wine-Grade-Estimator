from flask import Flask, request, jsonify, render_template
import os
import numpy as np
import pandas as pd
from src.pipeline.prediction import PredictionPipeline
from src.exception import CustomException
from src import logger
import sys

app= Flask(__name__)

@app.route('/',methods=['GET'])
def homePage():
    return render_template('index.html')


@app.route('/train', methods=['GET'])
def train():
    os.system("python application.py")
    return "Training completed successfully. The model has been trained and saved."

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('index.html', prediction = str(predict[0]))
        except Exception as e:
            logger.error(f"Error in prediction: {e}")
            raise CustomException(e, sys)
    else:
        return render_template('index.html')
    


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)