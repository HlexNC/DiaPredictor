from imblearn.over_sampling import SMOTENC
import pandas as pd

# Read the data
df = pd.read_csv('downsampled_dataset.csv')
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Convert categorical variables to numeric codes before SMOTE
valid_smoking_history = ['never', 'former', 'current', 'No Info']
X['smoking_history'] = pd.Categorical(X['smoking_history'], 
                                    categories=valid_smoking_history,
                                    ordered=False)
X['smoking_history'] = X['smoking_history'].cat.codes

# Get the indices of categorical features
categorical_features_indices = [X.columns.get_loc(col) for col in ['gender', 'smoking_history']]

# Apply SMOTE
smote = SMOTENC(random_state=42, 
                sampling_strategy=0.5, 
                k_neighbors=5, 
                categorical_features=categorical_features_indices)
X_res, y_res = smote.fit_resample(X, y)

# Convert smoking_history back to categories
X_res['smoking_history'] = pd.Categorical.from_codes(
    X_res['smoking_history'].astype('int'),
    categories=valid_smoking_history
)

# Create the resampled dataset
df_resampled = pd.concat([X_res, y_res], axis=1)
df_resampled.to_csv('smotted_dataset.csv', index=False)

# Print value counts to verify the results
print("Smoking history distribution:")
print(df_resampled['smoking_history'].value_counts())
print("\nTarget distribution:")
print(df_resampled['diabetes'].value_counts())