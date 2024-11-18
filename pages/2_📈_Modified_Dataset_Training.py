import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Page Configuration
st.set_page_config(page_title="Model Training Comparison", page_icon="📊")

# Main Title
st.markdown("# Model Training: Linear vs Logistic Regression on Original Dataset")

# Sidebar Header
st.sidebar.header("Training Comparison Settings")

# Information Text
st.write(
    """This page demonstrates the difference in results between training a
Linear Regression model and a Logistic Regression model using the original dataset.
Visualizations are provided to compare the models' performance and predictions."""
)
@st.cache_data
def open_database():
    data = pd.read_csv("Datasets/modified_dataset_probability.csv")
    return data

# Read the dataset
df = open_database()

# Shuffle the data
df = shuffle(df, random_state=42).reset_index(drop=True)

# Separate features and target
X = df.drop(columns=['diabetes'])
y = df['diabetes']

# Split: 70% training, 30% temporary set (which will be split into test and validation)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)

# Split the temporary set into 50% test and 50% validation
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Train Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Make predictions on the validation and test sets for Linear Regression
y_val_pred_lr = lr_model.predict(X_val)
y_test_pred_lr = lr_model.predict(X_test)

# Calculate MSE and R² for Linear Regression
mse_val_lr = mean_squared_error(y_val, y_val_pred_lr)
r2_val_lr = r2_score(y_val, y_val_pred_lr)
mse_test_lr = mean_squared_error(y_test, y_test_pred_lr)
r2_test_lr = r2_score(y_test, y_test_pred_lr)

# Initialize and train Random Forest Regressor
rf_model = DecisionTreeRegressor()
rf_model.fit(X_train, y_train)

# Make predictions on validation and test sets
y_val_pred_rf = rf_model.predict(X_val)
y_test_pred_rf = rf_model.predict(X_test)

# Calculate MSE and R² for Random Forest Regression
mse_val_rf = mean_squared_error(y_val, y_val_pred_rf)
r2_val_rf = r2_score(y_val, y_val_pred_rf)
mse_test_rf = mean_squared_error(y_test, y_test_pred_rf)
r2_test_rf = r2_score(y_test, y_test_pred_rf)

st.write(" R2: the greater the value, the better the model is predicting.")
st.write(" MSE: the lower the value, the better the model is predicting. ")

# Display results in a table
st.markdown("### Model Performance Summary")

st.write("""
| Metric                            | Linear Regression | Logistic Regression |
|-----------------------------------|-------------------|---------------------|
| **Validation MSE**                | {:.4f}            | {:.4f}              |
| **Validation R²**                 | {:.4f}            | {:.4f}              |
| **Test MSE**                      | {:.4f}            | {:.4f}              |
| **Test R²**                       | {:.4f}            | {:.4f}              |
""".format(
    mse_val_lr, mse_val_rf,
    r2_val_lr, r2_val_rf,
    mse_test_lr, mse_test_rf,
    r2_test_lr, r2_test_rf
))

# Plotting MSE and R² for both models
metrics = ['Validation MSE', 'Test MSE', 'Validation R²', 'Test R²']
linear_values = [mse_val_lr, mse_test_lr, r2_val_lr, r2_test_lr]
rf_values = [mse_val_rf, mse_test_rf, r2_val_rf, r2_test_rf]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Validation MSE
axes[0, 0].bar(['Linear', 'Logistic'], [mse_val_lr, mse_val_rf], color=['blue', 'orange'])
axes[0, 0].set_title('Validation MSE')
axes[0, 0].set_ylabel('Mean Squared Error')

# Test MSE
axes[0, 1].bar(['Linear', 'Logistic'], [mse_test_lr, mse_test_rf], color=['blue', 'orange'])
axes[0, 1].set_title('Test MSE')
axes[0, 1].set_ylabel('Mean Squared Error')

# Validation R²
axes[1, 0].bar(['Linear', 'Logistic'], [r2_val_lr, r2_val_rf], color=['blue', 'orange'])
axes[1, 0].set_title('Validation R²')
axes[1, 0].set_ylabel('R² Score')

# Test R²
axes[1, 1].bar(['Linear', 'Logistic'], [r2_test_lr, r2_test_rf], color=['blue', 'orange'])
axes[1, 1].set_title('Test R²')
axes[1, 1].set_ylabel('R² Score')

# Adjust layout
plt.tight_layout()

# Display the plots in Streamlit
st.pyplot(fig)
