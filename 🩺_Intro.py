import streamlit as st

# Page configuration
st.set_page_config(page_title="Diabetes Prediction Web App", page_icon="🩺", layout="centered")

# Main title
st.markdown("# Welcome to the Diabetes Prediction Web App")
st.write(
    """
    This web application is designed to provide insights into diabetes prediction by analyzing key health metrics
    and exploring the impact of data transformations on predictive modeling.
    """
)

# Purpose of the Web App
st.markdown("### Purpose")
st.write(
    """
    The main goal of this app is to:
    
    - Explore and visualize the dataset used for diabetes prediction.
    - Demonstrate how data preprocessing impacts model performance.
    - Compare different regression models and evaluate their accuracy in predicting diabetes probabilities.
    - Provide an interactive and intuitive way to understand the importance of data transformations in machine learning.
    """
)

# Overview of Features
st.markdown("### What This Web App Includes")
st.write(
    """
    - **Dataset Overview**:
      - A detailed look at the original and modified datasets, including their features, transformations, and key characteristics.
    - **Data Visualization**:
      - Interactive visualizations to uncover patterns and relationships in the dataset.
    - **Model Training**:
      - A comparison of regression models (Linear Regression and Decision Tree) for predicting diabetes probabilities.
    - **Performance Metrics**:
      - Insight into model performance through metrics such as Mean Squared Error (MSE) and R² Score.
    """
)

# Call to Action
st.markdown("### Navigate to Other Pages")
st.write(
    """
    Use the sidebar to explore each page:
    
    - **Dataset Overview**: Learn about the datasets and their transformations.
    - **Data Visualization**: Dive into visual patterns within the data.
    - **Model Training**: Understand how models are trained and compare their performance.
    """
)


