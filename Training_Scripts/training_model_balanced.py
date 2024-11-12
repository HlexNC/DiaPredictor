import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('/home/morningstar/Desktop/assistance-systems-project/Datasets/cat_to_num.csv')

# Separate features (X) and target (y)
X = df.drop('diabetes_1', axis=1)  # Use 'diabetes_1' as the target column
y = df['diabetes_1']

# Split: 70% training, 30% temporary set (which will be split into test and validation)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    random_state=104, 
                                                    shuffle=True)

# Split the temporary set into 50% test and 50% validation
X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, 
                                                              test_size=0.5, 
                                                              random_state=104, 
                                                              shuffle=True)

# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model on the validation set
y_valid_prob = model.predict_proba(X_valid)[:, 1]  # Get the probability for class 1 (diabetes)
mse_valid = mean_squared_error(y_valid, y_valid_prob)
print(f"Validation Mean Squared Error: {mse_valid}")

# Evaluate the model on the test set
y_test_prob = model.predict_proba(X_test)[:, 1]  # Get the probability for class 1 (diabetes)
mse_test = mean_squared_error(y_test, y_test_prob)
print(f"Test Mean Squared Error: {mse_test}")
