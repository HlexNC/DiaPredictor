import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#Load the data#read train.csv and store it in 'X'
X=pd.read_csv('../input/home-data-for-ml-course/train.csv',index_col='Id')#read test.csv and store it in 'X_test'
X_test=pd.read_csv('../input/home-data-for-ml-course/test.csv',index_col='Id')