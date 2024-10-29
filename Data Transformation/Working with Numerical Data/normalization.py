import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('smotted_dataset.csv')

scaler = MinMaxScaler()
df[['age', 'bmi', 'average_blood_glucose_level', 'current_blood_glucose_level']] = scaler.fit_transform(df[['age', 'bmi', 'average_blood_glucose_level', 'current_blood_glucose_level']])

df.to_csv('linear_scaled_dataset.csv', index=False)

