import numpy as np
from sklearn.preprocessing import  MinMaxScaler # For the normalization fo values
import joblib
import os

def normalize_inputs(inputs, smoking_history, hypertension, heart_disease):
    if smoking_history == "Never":
            smoking_history_encoded = 0  
    elif smoking_history == "Former":
        smoking_history_encoded = 1  
    else:
        smoking_history_encoded = 2  

    # Normalize hypertension value: "Yes"/"No" to 1/0
    if hypertension == "Yes" or hypertension == True:
        hypertension_normalized = 1  
    else:
        hypertension_normalized = 0 

    if heart_disease == "Yes" or heart_disease == True:
        heart_disease_normalized = 1
    else:
        heart_disease_normalized = 0

    inputs_2d = np.array(inputs).reshape(1, -1)

    # Normalizes input values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit([[0, 10.0, 4.0, 70.0], [100, 50.0, 14.0, 300.0]])    
    normalized_inputs = scaler.transform(inputs_2d)
    age, bmi, avg_glucose, current_glucose = normalized_inputs[0]

    smoking_history_normalized = smoking_history_encoded / 2  # Dividing by 2 to scale between 0 and 1

    # Prepare user input as a feature vector
    features = np.array([
        [
            age,
            bmi,
            avg_glucose,
            current_glucose,
            hypertension_normalized,             # Convert checkbox to binary
            heart_disease_normalized,            # Convert checkbox to binary
            smoking_history_normalized   # One-hot encoding for "Current"    
        ]
    ])

    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script  
    model_path = os.path.join(script_dir, "../Datasets/model.pkl")  # Go one level up, then to Datasets
    # Load the model and predict
    model = joblib.load(model_path)    
    prediction = model.predict(features)[0]  # Predict using the model

    print("This is the prediction: ", prediction)
    return prediction   