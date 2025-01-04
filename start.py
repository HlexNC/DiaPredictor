# This file was created in order to simplify the process of running everything. #
# It will start all the necessary services for the DiaPredictor application: the Rasa servers and the Streamlit webpage. It will train a model if one does not exist. #
import subprocess
import time
import sys
import os

def start_process(command, name):
    try:
        process = subprocess.Popen(command, shell=True)
        print(f"{name} started with PID {process.pid}.")
        return process
    except Exception as error:
        print(f"Failed to start {name}: {error}")
        return None

# Checks for model. Trains if no model present. #
def check_and_train_model():
    # Ensure we're in the Rasa project directory
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rasa_backend"))

    # Check if the Rasa model exists in the rasa_backend/models directory
    models_dir = os.path.join(os.getcwd(), "models")
    if not os.path.exists(models_dir) or not any(f.endswith(".tar.gz") for f in os.listdir(models_dir)):
        print("No Rasa model found. Training a new model...")
        train_command = "rasa train"
        try:
            subprocess.run(train_command, shell=True, check=True)
            print("Model training completed.")
        except subprocess.CalledProcessError as e:
            print(f"Model training failed: {e}")
            sys.exit(1)
    else:
        print("Rasa model found. Skipping training.")


if __name__ == "__main__":
    # Check if model exists 
    check_and_train_model()

    # Start Rasa server
    rasa_server_command = "rasa run --enable-api"
    rasa_server = start_process(rasa_server_command, "Rasa server")

    # Start Rasa actions server
    rasa_actions_command = "rasa run actions"
    rasa_actions = start_process(rasa_actions_command, "Rasa actions")

    # Start Streamlit app
    os.chdir(os.path.dirname(os.path.abspath(__file__))) # navigate back to root directory
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
