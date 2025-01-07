import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_and_save_model(data_path, save_path="Datasets/model.pkl"):
    """
    Trains a Linear Regression model on the modified dataset and saves it as a .pkl file.

    Parameters:
    - data_path: str, path to the dataset CSV file.
    - save_path: str, path where the trained model will be saved.
    
    Returns:
    - dict: Training results, including splits, metrics, and the trained model.
    """
    # Load the dataset
    df = pd.read_csv(data_path)
    df = shuffle(df, random_state=42).reset_index(drop=True)

    # Separate features and target
    X = df.drop(columns=['diabetes'])
    y = df['diabetes']

    # Split: 70% training, 30% temporary set (which will be split into test and validation)
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)

    # Split the temporary set into 50% test and 50% validation
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # Train Linear Regression model
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)

    # Save the model
    joblib.dump(lr_model, save_path)

    return {
        "model": lr_model,
        "splits": {"X_train": X_train, "X_val": X_val, "X_test": X_test, 
                   "y_train": y_train, "y_val": y_val, "y_test": y_test},
        "metrics": {"X_val": X_val, "y_val": y_val, 
                    "X_test": X_test, "y_test": y_test}
    }
