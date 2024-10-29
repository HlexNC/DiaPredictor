import pandas as pd

df = pd.read_csv('smotted_dataset.csv')

df['age'] = df['age'].round(0).astype(int)
df['hypertension'] = df['hypertension'].round(0).astype(int)
df['heart_disease'] = df['heart_disease'].round(0).astype(int)

df.to_csv('smotted_dataset2.csv', index=False)