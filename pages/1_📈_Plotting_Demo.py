import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Read the dataset
df = pd.read_csv('/home/morningstar/Desktop/assistance-systems-project/Datasets/cleaned_normalized_dataset.csv')

# Separate features (X) and target (y)
X = df.drop('diabetes_1', axis=1)
y = df['diabetes_1']

# Split: 70% training, 30% temporary set (which will be split into test and validation)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    random_state=104, 
                                                    shuffle=True)

# Split the temporary set into 50% test and 50% validation
X_validation, X_test, y_validation, y_test = train_test_split(X_temp, y_temp, 
                                                              test_size=0.5, 
                                                              random_state=104, 
                                                              shuffle=True)

# Train model with train data
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict for validation dataset
y_valid_prob = model.predict_proba(X_validation)[:, 1]  # We take the probability for class 1 (diabetes)
mse_valid = mean_squared_error(y_validation, y_valid_prob)

print(f"Validation Mean Squared Error: {mse_valid}")

# Predict for test dataset
y_test_prob = model.predict_proba(X_test)[:, 1]  # We take the probability for class 1 (diabetes)
mse_test = mean_squared_error(y_test, y_test_prob)

print(f"Test Mean Squared Error: {mse_test}")
