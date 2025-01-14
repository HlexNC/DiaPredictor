import numpy as np
from sklearn.preprocessing import  MinMaxScaler # For the normalization fo values
import joblib
import pandas as pd
import os

def normalize_inputs(inputs, smoking_history, hypertension, heart_disease):
    if smoking_history == "Never":
            smoking_history_encoded = 0  
    elif smoking_history == "Former":
        smoking_history_encoded = 1  
    else:
        smoking_history_encoded = 2  

    # Normalize hypertension value: "Yes"/"No" to 1/0
    if not isinstance(hypertension, bool):
        if hypertension.lower() == "yes" or hypertension == True:
            hypertension = 1  
        else:
            hypertension = 0 

    if not isinstance(heart_disease, bool):
        if heart_disease.lower() == "yes" or heart_disease == True:
            heart_disease = 1
        else:
            heart_disease = 0

    inputs_2d = np.array(inputs)

    # Normalizes input values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit([[0, 10.0, 4.0, 70.0], [100, 50.0, 14.0, 300.0]])    
    normalized_inputs = scaler.transform(inputs_2d)
    age, bmi, avg_glucose, current_glucose = normalized_inputs[0]

    smoking_history_normalized = smoking_history_encoded / 2  # Dividing by 2 to scale between 0 and 1

    feature_names = [
    "age", 
    "bmi", 
    "average_blood_glucose_level", 
    "current_blood_glucose_level", 
    "hypertension_1", 
    "heart_disease_1", 
    "smoking_history_former"
]

    features = pd.DataFrame(np.array([
        [
            age,
            bmi,
            avg_glucose,
            current_glucose,
            hypertension,  # Convert checkbox to binary
            heart_disease,  # Convert checkbox to binary
            smoking_history_normalized  # One-hot encoding for "Current"
        ]
    ]), columns=feature_names)

    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script  
    model_path = os.path.join(script_dir, "../Datasets/model.pkl")  # Go one level up, then to Datasets
    # Load the model and predict
    model = joblib.load(model_path)    
    prediction = model.predict(features)[0]  # Predict using the model

    print("This is the prediction: ", prediction)
    return prediction   