import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Modified Dataset Overview", page_icon="📊")

# Page title and description
st.markdown("# Modified Diabetes Prediction Dataset Overview")
st.write(
    """
    This page provides details about the **Modified Diabetes Prediction Dataset** and highlights the transformations applied to enhance its suitability for analysis and modeling.
    
    ### Key Transformations:
    
    1. **Removal of Incomplete Examples**:
       - Any missing or incomplete rows in the dataset were removed to ensure data quality.
    
    2. **Balancing the Dataset**:
       - The dataset initially had an approximate ratio of 10:1 (non-diabetic to diabetic cases). This imbalance was addressed by:
         - **Downsampling** the majority class by 80%.
         - **Oversampling** the minority class using the SMOTENC method to synthesize new examples while reducing overfitting risks.
    
    3. **Column Removal**:
       - Features with minimal impact on predicting diabetes (e.g., "Gender" and "Never Smoked") were excluded.
    
    4. **Probability-Based Target**:
       - The `diabetes` target column was converted from binary labels (`0` or `1`) to a probability, influenced by key factors like **age**. The probabilities are random but biased toward attributes with higher predictive power.
    """
)

@st.cache_data
def load_modified_dataset():
    return pd.read_csv('Datasets/modified_dataset.csv')

# Load the modified dataset
modified_df = load_modified_dataset()

# Display the modified dataset
st.markdown("## Modified Dataset Sample")
st.write("Here is a sample of the **Modified Diabetes Prediction Dataset**:")
st.write(modified_df.head())

st.markdown("### Modified Dataset Summary")
st.write("Below is the statistical summary of the modified dataset:")
st.write(modified_df.describe())

# Highlight Differences
st.markdown("## Key Characteristics of the Modified Dataset")
st.write(
    """
    - **Balanced Dataset**:
      - The dataset is more balanced compared to its original version, addressing the class imbalance issue.
    - **Cleaned Data**:
      - All missing or incomplete rows have been removed for better data quality.
    - **Target Variable Transformation**:
      - The `diabetes` column represents probabilities instead of binary labels.
    - **Feature Selection**:
      - Non-informative features like "Gender" and "Never Smoked" have been excluded.
    """
)
