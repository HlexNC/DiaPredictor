from imblearn.under_sampling import RandomUnderSampler
import pandas as pd

df = pd.read_csv('cleaned_dataset.csv')

X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Undersampling the majority class
# Sampling Strategy allows to remove a certain percentage of the majority in this case. Currently, we undersample by a factor of 5.#
# Ratio is 5:1 for non-diabetics 
rus = RandomUnderSampler(random_state=42, sampling_strategy = 0.2)
X_res, y_res = rus.fit_resample(X, y)

# Ratio after undersampling
ratio = 42410 / 8482
#print(X_res.value_counts(), y_res.value_counts(), f"Ratio: {ratio}")
df_resampled = pd.concat([X_res, y_res], axis=1)
df_resampled['age'] = df_resampled['age'].astype(int)
df_resampled.to_csv('downsampled_dataset.csv', index=False) # Creates a different file with removed majority #