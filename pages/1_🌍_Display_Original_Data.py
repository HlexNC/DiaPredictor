import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Dataset Overview", page_icon="📊")

# Page title and description
st.markdown("# Diabetes Prediction Dataset Overview")
st.write(
    """
    This dataset is designed for predicting diabetes status based on several health indicators and lifestyle factors. Below is an overview of the dataset's features:
    
    - **Gender**: Represents the gender of the individual, with values as "Male" or "Female".
    - **Age**: The age of the individual, represented as an integer.
    - **Hypertension**: Indicates high blood pressure presence. It is binary: `0 = No`, `1 = Yes`.
    - **Heart Disease**: Indicates heart disease presence. It is binary: `0 = No`, `1 = Yes`.
    - **Smoking History**: Categorical data that represents smoking status, such as "never smoked," "used to smoke," or "currently smoking."
    - **BMI (Body Mass Index)**: A measure of body fat based on height and weight, represented by float values.
    - **Average Blood Glucose Level**: The average blood glucose level over the past 2-3 months, usually used to monitor diabetes. Represented as floats, typically between `4.0` to `14.0`.
    - **Blood Glucose Level**: The current blood glucose level, typically represented by float values starting from `80 mg/dL` and above.
    - **Diabetes**: Indicates if the individual has diabetes, where `0 = No` and `1 = Yes`.
    """
)

# Load the dataset
df = pd.read_csv('Datasets/original_dataset.csv')

# Display the dataset
st.markdown("## Dataset Sample")
st.write("Here is a preview of the dataset used for the diabetes prediction task:")
st.write(df.head())

# Display dataset information
st.markdown("## Dataset Details")
st.write("The dataset contains the following columns and data types:")
st.write(df.describe())
