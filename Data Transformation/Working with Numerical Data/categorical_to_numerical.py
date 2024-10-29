import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Read the dataset
df = pd.read_csv('Data Transformation/linear_scaled_dataset.csv')

# Extract categorical columns from the dataframe
categorical_columns = ['gender', 'hypertension', 'heart_disease', 'smoking_history', 'diabetes']

# Initialize OneHotEncoder (dropping the first category to avoid redundant columns)
encoder = OneHotEncoder(sparse_output=False, drop='first')

# Apply one-hot encoding to the categorical columns
one_hot_encoded = encoder.fit_transform(df[categorical_columns])

# Create a DataFrame with the one-hot encoded columns
one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

# Create a DataFrame for the original numerical columns
numerical_columns = ['age', 'bmi', 'average_blood_glucose_level', 'current_blood_glucose_level']
numerical_df = df[numerical_columns]

# Concatenate the one-hot encoded dataframe with the original numerical dataframe
df_encoded = pd.concat([numerical_df, one_hot_df], axis=1)

# Save the encoded DataFrame to a CSV file
df_encoded.to_csv('cat_to_num.csv', index=False)
