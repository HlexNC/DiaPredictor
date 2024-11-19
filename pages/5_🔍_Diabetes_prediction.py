import streamlit as st
import numpy as np
import joblib  # For loading the saved model

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
avg_glucose = st.number_input("Average Blood Glucose Level (mmol/L)", min_value=4.0, max_value=14.0, value=5.5, step=0.1)
current_glucose = st.number_input("Current Blood Glucose Level (mmol/L)", min_value=4.0, max_value=14.0, value=5.5, step=0.1)
# Dropdown for Smoking History
smoking_history = st.selectbox(
    "Smoking History",
    options=["Never", "Former", "Current"],
    index=0
)

# Prepare user input as a feature vector
feature_vector = np.array([
    [
        age,
        bmi,
        avg_glucose,
        current_glucose,
        int(hypertension),             # Convert checkbox to binary
        int(heart_disease),            # Convert checkbox to binary
        1 if smoking_history == "Former" else 0
    ]
])

# Button to trigger prediction
if st.button("Predict Diabetes Risk"):
    # Load your trained model (replace 'model.pkl' with your model's filename)
    try:
        model = load_model()
        prediction = model.predict(feature_vector)[0]  # Predict using the model
        st.success(f"Predicted Diabetes Probability: {prediction:.2f}")
        if prediction > 0.5:
            st.warning("You might be at risk for diabetes. Consider consulting a healthcare professional.")
        else:
            st.info("You have a low risk of diabetes. Keep maintaining a healthy lifestyle!")
    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model file is in the correct location.")

