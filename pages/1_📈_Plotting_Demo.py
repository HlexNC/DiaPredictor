import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
@st.cache_data
def open_database():
    data = pd.read_csv("Datasets/cat_to_num.csv")
    return data

data = open_database()
data = shuffle(data, random_state=42).reset_index(drop=True)
X = data.drop(columns=['diabetes_1'])
y = data['diabetes_1']
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)  # 70% training, 30% temp
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)  # 15% validation, 15% test

# Step 1: Train Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_val_pred_linear = linear_model.predict(X_val)
y_test_pred_linear = linear_model.predict(X_test)

# Step 2: Train Logistic Regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
y_val_pred_logistic = logistic_model.predict(X_val)
y_test_pred_logistic = logistic_model.predict(X_test)

# Step 3: Calculate the loss (MSE) and R² for both models on the validation and test sets
# Linear Regression on Validation
mse_val_linear = mean_squared_error(y_val, y_val_pred_linear)
r2_val_linear = r2_score(y_val, y_val_pred_linear)

# Logistic Regression on Validation
mse_val_logistic = mean_squared_error(y_val, y_val_pred_logistic)  # Mean Squared Error for comparison
accuracy_val_logistic = accuracy_score(y_val, y_val_pred_logistic)

# Linear Regression on Test
mse_test_linear = mean_squared_error(y_test, y_test_pred_linear)
r2_test_linear = r2_score(y_test, y_test_pred_linear)

# Logistic Regression on Test
mse_test_logistic = mean_squared_error(y_test, y_test_pred_logistic)
accuracy_test_logistic = accuracy_score(y_test, y_test_pred_logistic)

# Display validation and test results
st.write("Validation Results:")
st.write("Linear Regression - MSE:", mse_val_linear)
st.write("Linear Regression - R²:", r2_val_linear)
st.write("Logistic Regression - MSE (for comparison):", mse_val_logistic)
st.write("Logistic Regression - Accuracy:", accuracy_val_logistic)

st.write("Test Results:")
st.write("Linear Regression - MSE:", mse_test_linear)
st.write("Linear Regression - R²:", r2_test_linear)
st.write("Logistic Regression - MSE (for comparison):", mse_test_logistic)
st.write("Logistic Regression - Accuracy:", accuracy_test_logistic)

# Step 4: Plot predictions from both models on the same graph for comparison
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_test_pred_linear, color='blue', alpha=0.5, label="Linear Regression Predictions")
plt.scatter(y_test, y_test_pred_logistic, color='green', alpha=0.5, label="Logistic Regression Predictions")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, label="Perfect Prediction Line")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Comparison of Predictions from Linear and Logistic Regression Models (Test Set)")
plt.legend()

# Show the plot in Streamlit
st.pyplot(plt)

st.write("Sine Logistic regression has higher accuracy number, it is better for this dataset")

