import streamlit as st
import time
from sklearn.utils import shuffle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, f1_score

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

data = pd.read_csv("Datasets/cat_to_num.csv")
data = shuffle(data, random_state=42).reset_index(drop=True)
X = data.drop(columns=['diabetes_1'])
y = data['diabetes_1']
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)  # 70% training, 30% temp
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)  # 15% validation, 15% test

model = LinearRegression()
model.fit(X_train, y_train)

# 1. Make predictions on the validation set
y_val_pred = model.predict(X_val)

# 2. Evaluate the predictions
# Choose appropriate metrics based on your task

# For regression:
mse = mean_squared_error(y_val, y_val_pred)
r2 = r2_score(y_val, y_val_pred)
print("Validation Mean Squared Error:", mse)
print("Validation R-squared:", r2)



