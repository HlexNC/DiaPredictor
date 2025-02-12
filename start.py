import subprocess
import time
import sys
import os
from Additional_Scripts.model_training import train_and_save_model

def start_process(command, name):
    try:
        process = subprocess.Popen(command, shell=True)
        print(f"{name} started with PID {process.pid}.")
        return process
    except Exception as error:
        print(f"Failed to start {name}: {error}")
        return None

# Checks for the Rasa model. Trains if no model is present. #
def check_and_train_rasa_model():
    # Ensure we're in the Rasa project directory
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rasa_backend"))

    # Check if the Rasa model exists in the rasa_backend/models directory
    models_dir = os.path.join(os.getcwd(), "models")
    if not os.path.exists(models_dir) or not any(f.endswith(".tar.gz") for f in os.listdir(models_dir)):
        print("No Rasa model found. Training a new model...")
        train_command = "rasa train"
        try:
            subprocess.run(train_command, shell=True, check=True)
            print("Rasa model training completed.")
        except subprocess.CalledProcessError as e:
            print(f"Rasa model training failed: {e}")
            sys.exit(1)
    else:
        print("Rasa model found. Skipping training.")

# Check for the model.pkl file. Train if it doesn't exist. #
def check_and_train_diabetes_model():
    datasets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Datasets")
    model_path = os.path.join(datasets_dir, "model.pkl")
    dataset_path = os.path.join(datasets_dir, "modified_dataset.csv")

    if not os.path.exists(model_path):
        print("No diabetes model (model.pkl) found. Training a new model...")
        try:
            train_and_save_model(dataset_path,save_path=model_path)
            print("Diabetes model training completed and saved as model.pkl.")
        except Exception as e:
            print(f"Diabetes model training failed: {e}")
            sys.exit(1)
    else:
        print("Diabetes model (model.pkl) found. Skipping training.")

if __name__ == "__main__":
    # Check and train the Rasa model
    check_and_train_rasa_model()

    # Check and train the diabetes model
    check_and_train_diabetes_model()

    # Start Rasa server
    rasa_server_command = "rasa run --enable-api"
    rasa_server = start_process(rasa_server_command, "Rasa server")

    # Start Rasa actions server
    rasa_actions_command = "rasa run actions"
    rasa_actions = start_process(rasa_actions_command, "Rasa actions")

    # Start Streamlit app
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Navigate back to root directory
    streamlit_command = "streamlit run 🩺_Intro.py"
    streamlit_app = start_process(streamlit_command, "Streamlit app")

    try:
        print("All processes started. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        print("Stopping all processes...")
        for process, name in [(rasa_server, "Rasa server"), (rasa_actions, "Rasa actions"), (streamlit_app, "Streamlit app")]:
            if process:
                process.terminate()
                print(f"{name} stopped.")
