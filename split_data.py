from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('smotted_dataset.csv')
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# First split
X_train, X_test, y_train, y_test = train_test_split(X,y , 
                                   random_state=104,  
                                   test_size=0.3,  
                                   shuffle=True)

df_train = pd.concat([X_train, y_train], axis=1)
df_test = pd.concat([X_test, y_test], axis = 1)

df_train.to_csv('train_dataset.csv', index = False, float_format='%.2f')

# Second split
X = df_test.drop('diabetes', axis=1)
y = df_test['diabetes']
X_validation, X_test, y_validation, y_test = train_test_split(X,y , 
                                            random_state=104,  
                                            test_size=0.5,  
                                            shuffle=True)

df_test = pd.concat([X_test, y_test], axis = 1)
df_validation = pd.concat([X_validation, y_validation], axis = 1)

df_test.to_csv('test_dataset.csv', index= False, float_format='%.2f')
df_validation.to_csv('validation_dataset.csv', index= False, float_format='%.2f')