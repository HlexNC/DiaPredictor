import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# For term documentation, please visit the Wiki on GitLab: Statistical Term Documentation #

df = pd.read_csv('cleaned_dataset.csv')

#Show ratio through chart
#sns.countplot(x='diabetes', data=df)

# Age Distribution
sns.histplot(data=df, x='age', hue='diabetes', multiple='stack')

# Blood Glucose Levels Distribution
#sns.histplot(data=df, x='current_blood_glucose_level', hue='diabetes', multiple='stack')

#HbA1c_level
#sns.histplot(data=df, x='average_blood_glucose_level', hue='diabetes', multiple='stack')

# Weight Distribution
# Plot KDE for BMI with diabetes status
#sns.kdeplot(data=df, x='bmi', hue='diabetes', fill=True)

numerical_df = df.select_dtypes(include=['float64', 'int64']).drop(columns=['hypertension', 'heart_disease', 'diabetes'])
# Mean and Median
print("Median:", numerical_df.median(), "\n")
print("Mean:", numerical_df.mean(), "\n")

# Standard Deviation
print("Standard Deviation:", numerical_df.std())

# The values at the quartile divisions
print(numerical_df.quantile(q=[0.25, 0.5, 0.75], axis=0, numeric_only=True))

plt.show()
