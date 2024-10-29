import pandas as pd

df = pd.read_csv('cleaned_dataset.csv')
df.dropna()
df = df.drop_duplicates()
df.reset_index(drop=True, inplace=True)

df.to_csv('cleaned_dataset.csv', index=False)