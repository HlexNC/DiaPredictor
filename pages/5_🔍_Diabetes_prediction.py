import streamlit as st
import pandas as pd
import numpy as np
import joblib  # For loading the saved model
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Additional_Scripts.normalizing_inputs_and_prediction import normalize_inputs

# Page configuration
st.set_page_config(page_title="Diabetes Prediction", page_icon="🔍")

# Page title and description
st.markdown("# Diabetes Risk Prediction")
st.write(
    """
    Enter your health and lifestyle details below to calculate your risk of having diabetes.
    This tool uses a machine learning model to provide predictions based on the entered data.
    """
)
# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("Datasets/model.pkl")


# Input Widgets
age = st.slider("Age", min_value=0, max_value=100, value=30, step=1)
hypertension = st.checkbox("Do you have hypertension?", value=False)
heart_disease = st.checkbox("Do you have heart disease?", value=False)
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0, step=0.1)

average_glucose = st.number_input("HbA1c Level (%)", 
                       min_value=4.0, 
                       max_value=14.0, 
                       value=5.5, 
                       step=0.1,
                       help="Normal: Below 5.7%\nPrediabetes: 5.7% to 6.4%\nDiabetes: 6.5% or above")

current_glucose = st.number_input("Current Blood Glucose Level (mg/dL)", 
                                min_value=70.0, 
                                max_value=300.0, 
                                value=100.0, 
                                step=1.0,
                                help="Normal fasting: 70-100 mg/dL\nPrediabetes: 100-125 mg/dL\nDiabetes: ≥126 mg/dL")


# Dropdown for Smoking History
smoking_history = st.selectbox(
    "Smoking History",
    options=["Never", "Former", "Current"],
    index=0
)

# Normalizes input values
inputs = [[age, bmi, average_glucose, current_glucose]]

# Prepare user input as a feature vector
feature_vector = normalize_inputs(inputs, smoking_history, hypertension, heart_disease)


# Button to trigger prediction
if st.button("Predict Diabetes Risk"):
    # Load your trained model (replace 'model.pkl' with your model's filename)
    try:
        prediction = normalize_inputs(inputs, smoking_history, hypertension, heart_disease)
        st.success(f"Predicted Diabetes Probability: {prediction:.2f}")

        # Bar to show severity of prediction 
        progress_percentage = int(prediction * 100)
        color = "background-color: red;" if progress_percentage > 50 else "background-color: green;"

        # Display the progress bar with percentage value
        st.markdown(
            f"""
            <div style="width: 100%; height: 30px; border-radius: 5px; {color} width: {progress_percentage}%;"></div>
            <span style="color: black; font-weight: bold; position: absolute; width: 100%; text-align: center; line-height: 30px;">
                {progress_percentage}%
            </span>
            """, 
            unsafe_allow_html=True
        )


        if prediction > 0.5:
            st.warning("You might be at risk for diabetes. Consider consulting a healthcare professional.")
        else:
            st.info("You have a low risk of diabetes. Keep maintaining a healthy lifestyle!")

    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model file is in the correct location.")

