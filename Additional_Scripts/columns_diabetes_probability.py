import pandas as pd
import numpy as np

# Read the dataset
df = pd.read_csv('/home/morningstar/Desktop/assistance-systems-project/Datasets/modified_dataset.csv')

# Drop columns we don't need
df.drop(columns=['gender_Male', 'gender_Other', 'smoking_current', 'smoking_history_nan', 'smoking_history_never'], axis=1, inplace=True)

# Set random seed for reproducibility
np.random.seed(42)

# Remove the diabetes columns from the dataset entirely
df = df.drop(columns=['diabetes_1'])

# Create a basic probability score (this is where we combine factors)
# The numbers by which we multiply are weights
df['diabetes'] = (
    0.1 * df['age'] +  # Age factor
    0.2 * df['bmi'] +  # BMI factor
    0.2 * df['average_blood_glucose_level'] +  # Average blood glucose level
    0.2 * df['current_blood_glucose_level'] +  # Current blood glucose level
    0.1 * df['hypertension_1'] +  # Hypertension history (1 = has hypertension)
    0.2 * df['heart_disease_1'] + 
    0.1 * df['smoking_history_former'] 
)

# Add random noise to introduce variability
df['diabetes'] += np.random.uniform(0, 0.2, size=len(df))

# Clip the values to ensure they are between 0 and 1
df['diabetes'] = df['diabetes'].clip(0, 1)

# Save the modified dataset with the new target variable
df.to_csv('/home/morningstar/Desktop/assistance-systems-project/Datasets/modified_with_sick_prob.csv', index=False)

print("Target variable 'probability_of_getting_sick' added and file saved.")
