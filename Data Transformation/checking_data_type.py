import pandas as pd

# Load your dataset (assuming it's in CSV format)
df = pd.read_csv('train_dataset.csv')

# Check class distribution for the target variable (assuming 'diabetes' is the target variable)
class_counts = df['diabetes'].value_counts()

# Calculate the percentage of each class
class_percentages = class_counts / len(df) * 100

# Calculate the ratio (majority class to minority class) as an integer
ratio = int(class_counts[0] / class_counts[1])

# Print the class distribution as percentages
print("Class Distribution (Percentages):")
print(class_percentages)

# Print the ratio of majority class to minority class
