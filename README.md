Firstname2, Lastname2, 12345

Firstname1, Lastname1, 12345

DiaPredictor

https://github.com/FaresM7/DiaPredictor

https://github.com/FaresM7/DiaPredictor/-/wikis/home

## Project Description

**Diapredictor** is an innovative system designed to assist individuals in assessing their risk for diabetes.  

The project begins with a dataset that has been meticulously cleaned and enriched with synthetic data to simulate diverse user scenarios. Multiple machine learning models have been trained and evaluated on both the original and the augmented datasets to ensure robustness and accuracy.  

The project features dedicated pages that display:  
- The original dataset.  
- The modified dataset.  
- Comparisons of two models trained on the original data to identify the better performer.  
- Comparisons of two models trained on the modified data to determine the best approach for the enriched dataset.  

The system comprises two primary user-centric components:  
1. **Chatbot Assistant**: A conversational AI that interacts with users to gather health-related information, assess their potential risk of diabetes, and provide personalized lifestyle tips to improve their health.  
2. **Predictor System**: A direct interface where users can input specific health data and receive an immediate assessment of their likelihood of having diabetes.  

This comprehensive approach positions Diapredictor as both a diagnostic tool and an educational platform, empowering users to make informed decisions about their health.


## Installation

Prerequisites:

- **Python**: version 3.10
- **Git**: For cloning the repository and managing submodules.
- The rest of the requirements are included in the requirements.txt file and are installed if the script was followed

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/FaresM7/DiaPredictor

2. Create a virtual environment with Python 3.10
   ```bash
   py -3.10 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install the required dependencies
   ```bash
   pip install -r requirements.txt

4. Run the application
   ```bash
   python start.py
5. In case you were not redirected to the Streamlit pages you can open your browser and navigate to:
http://localhost:8501

## Data

### Original dataset

We used the [Diabetes prediction dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) from Kaggle for training the models and later enhance the dataset.

### Data Analysis Before Transformation
Initial data visualization revealed the following:
- A slight drop in diabetes cases between ages 60–70, followed by a sharp increase at 80+.
- Minimal differences in diabetes cases between males and females.
- Nearly symmetrical distribution with minimal differences between mean and median values.
- Quartiles exhibited expected variations across attributes.

### Data Cleaning and Handling
- **Incomplete Data:** Removed incomplete examples using Pandas. Labels were verified to ensure direct labeling.
- **Balancing:** The dataset originally had a 10:1 imbalance favoring non-diabetic cases.
  - **Downsampling:** Majority class reduced to 20% (1:2 ratio).
  - **Oversampling:** SMOTENC (Synthetic Minority Over-sampling for Nominal and Continuous data) was applied to the minority class to balance the dataset while addressing potential overfitting concerns.

### Transformations Applied to Original and Modified Datasets
1. **Splitting:** Dataset divided into Training (70%), Validation (15%), and Test (15%) sets. Initial splits showed a 1:3 imbalance for diabetic cases.
2. **Categorical Data Encoding:** Hot-end encoding converted categorical features into binary columns for model training.
3. **Normalization:** Linear scaling normalized feature values, addressing right-skewed distributions (e.g., age). Z-Score standardization was avoided due to non-normal distributions and minimal outliers.
4. **Removal of Unnecessary Attributes:** Attributes with minimal model impact (e.g., gender, certain smoking history categories) were excluded from the modified dataset.

### Post-Balancing Observations
- Diabetes correlation with age showed a zigzag pattern, with a sharp increase in cases at ages 75–80.
- Slight gender differences in diabetes cases remained.
- Blood glucose levels displayed increased variation after SMOTENC, with standard deviation rising from 40.90 to 52.55.
- Quartiles maintained expected variation, with slightly increased spread compared to the original dataset.

## Basic usage

### Diabetes Prediction

#### Navigate to Diabetes Prediction:
- From the sidebar, select **Diabetes Prediction**.

#### Input Your Health Metrics:
- Enter your personal details such as age, BMI, glucose levels, smoking status, blood pressure, etc.

#### Receive Your Diabetes Risk Assessment:
- The system will calculate and display your diabetes risk along with actionable recommendations to reduce the risk, if applicable.

### Model Performance Analysis

#### Navigate to Model Analysis:
- Select **Modified dataset training** or **Original dataset training** from the sidebar.

#### Compare Training Results:
- Analyze the performance of models trained on both the original and modified datasets.
- View metrics such as **accuracy**, **precision**, **MSE**, and **R^2** for each model.

#### Visualize Model Performance:
- Explore visualizations like **Bar charts** to understand how the models perform and identify strengths or weaknesses.


### Chatbot Assistance

#### Access the Chatbot:
- Click on **Chatbot** in the sidebar to open the conversational assistant.

#### Interact with the Chatbot:
- Ask questions related to diabetes risk, health tips, or dataset insights.
- Receive real-time, context-aware responses to help you understand and manage your health better.

### Dataset Analysis

#### Navigate to Dataset Overview:
- From the sidebar, select **Display original data** or **Display modified data**.

#### Explore Dataset Samples:
- View samples from both the **original** and **modified** datasets to understand their structure and key features.

#### Analyze Dataset Statistics:
- Examine summary statistics like **mean**, **median**, **standard deviation**, and **distribution** for important features such as **age**, **BMI**, and **glucose levels**.
- Compare how these statistics differ between the original and modified datasets to understand the impact of data preprocessing and enrichment.

### Implementation of the Requests
#### Introduction Page

This page sets up the initial configuration and layout for the web app. The `st.set_page_config` function is used to define the page title, icon, and layout style. The title and introductory text explain the purpose of the web app. This section also outlines the app's key features, such as dataset exploration, data visualizations, and model comparison. Finally, users are encouraged to use the sidebar to navigate through other sections of the app.

*The entirety of the page was handled by Name1 Elbermawy.*

#### Original and Modified Dataset Overview Page

These pages provide overviews of the datasets. The page of the modified dataset outlines the key transformations applied to improve its quality and suitability for analysis. 

The `st.set_page_config` function sets the page title and icon. The dataset is loaded using the `load_modified_dataset` function, which uses `pandas` to read the dataset from a CSV file. The page then displays a sample of the dataset and its statistical summary using `st.write`.

*The entirety of the page was handled by Name1 Elbermawy.*

#### Model Training Comparison Page Code Explanation

These pages compare the performance of two models, Linear Regression and Decision Tree, on the original and modified datasets.

1. **Page Setup**: The `st.set_page_config` function configures the page's title and icon. The page then shows a progress bar (`st.progress`) that updates during the model training process.

2. **Model Training**:
   - The `load_model_and_data` function loads the dataset and trains the models using the `train_and_save_model` function, which is imported from an external script.
   - The results contain the trained models, data splits (training, validation, and test sets), and evaluation metrics (Mean Squared Error and R² Score).

3. **Model Evaluation**:
   - Linear Regression and Decision Tree models are evaluated on both validation and test data.
   - The metrics (MSE and R²) are calculated for both models using `mean_squared_error` and `r2_score` from `sklearn.metrics`.

4. **Results Display**:
   - The performance metrics are displayed in a table format using `st.write`.
   - Visualizations of MSE and R² scores for both models are plotted using `matplotlib`. Four bar plots are created to compare the models' performance for both validation and test sets.

5. **Interactive Features**: The page includes interactive elements like a progress bar to indicate training progress and displays the performance comparison in both text and graphical formats.

*The entirety of the page was handled by Name1 Elbermawy.*

### Diabetes Risk Prediction Page Explanation

#### **1. Page Configuration:**
- `st.set_page_config(page_title="Diabetes Prediction", page_icon="🔍")`: Configures the page's title and icon.
- `st.markdown` and `st.write`: Display the page title and a short description about the diabetes risk prediction tool.

#### **2. Model Loading:**
- The model is loaded using `joblib.load("Datasets/model.pkl")`. 
- The `@st.cache_resource` decorator is used to cache the model, which improves performance by avoiding repeated loading during interactions.

#### **3. Input Widgets:**
- **Age**: A slider (`st.slider`) allows the user to select their age.
- **Hypertension** and **Heart Disease**: `st.checkbox` lets users indicate if they have these conditions.
- **BMI, Average Glucose, Current Glucose**: `st.number_input` is used for users to input these values.
- **Smoking History**: A dropdown (`st.selectbox`) lets users choose between "Never", "Former", and "Current" smoking history.

#### **4. Normalization of Inputs:**
- The inputs are gathered into a list (`inputs = [[age, bmi, average_glucose, current_glucose]]`) and passed to the `normalize_inputs` function, which likely processes and scales the data for the model.

#### **5. Prediction Button:**
- When the **"Predict Diabetes Risk"** button is clicked (`st.button`), the code:
  - Attempts to normalize the inputs and make a prediction.
  - Displays the predicted diabetes probability using `st.success`.
  - Creates a progress bar to visually show the prediction's severity, with red indicating higher risk and green for lower risk.
  - Provides a message based on the prediction:
    - **Low**: The user is unlikely to have diabetes.
    - **Moderate**: The user is at moderate risk and should consider lifestyle changes.
    - **High**: The user is at high risk and should consult a doctor.

#### **6. Error Handling:**
- If the model file is not found, an error message is shown using `st.error`.

*Name1 worked on most of this page. Name2 worked on the normalization of the data, such that the model could predict.*

### Chatbot Interface with Rasa and Streamlit
#### **1. Importing Libraries:**
- `streamlit`: For building the web interface.
- `json`: For handling JSON data.
- `requests`: To interact with Rasa's REST API.
- `time`: For implementing waiting periods in case of server unavailability.

#### **2. Function Definitions:**

 **check_server_ready():**
- Checks if the Rasa server is running and ready to handle requests by sending a GET request to the `/status` endpoint of the Rasa server.
- If the server is down, it waits for 5 seconds and retries until the server responds with a `200 OK` status.

 **get_bot_response(user_input):**
- Sends the user's input message to the Rasa bot using a POST request to the `/webhooks/rest/webhook` endpoint.
- Handles the response:
  - If the response contains multiple bot replies (in a list), it extracts the text from each response and appends it to `bot_responses`.
  - If there’s no text response or if the response is empty, it adds a default message asking the user to repeat the input.
  - If there’s a connection or request error, it returns an error message describing the problem.

#### **3. Streamlit Page Setup:**
- `st.set_page_config`: Configures the page title and layout.
- The page is configured to be wide with a title "Chatbot Interface" and a welcome message.

#### **4. Server Readiness Check:**
- If the server is not already marked as "ready" in `st.session_state`, the app checks if the Rasa server is available by calling the `check_server_ready()` function inside a spinner to indicate loading.

#### **5. Displaying Chat History:**
- If the server is ready, the chat interface initializes the session state with an empty list of messages (if not already present).
- It then displays the entire chat history by looping through the messages stored in `st.session_state["messages"]`.

#### **6. Handling User Input:**
- `st.chat_input`: A chat input field where users can type their message.
- If the user submits a message (`prompt`), the message is added to the session state under `"messages"` as a user message.

#### **7. Communicating with the Bot:**
- The user's input is sent to Rasa using `get_bot_response()`, and the bot’s responses are appended to the session state.
- The bot responses are displayed in the chat interface, where each response from the bot is shown under an "assistant" role.

#### **8. Displaying Responses:**
- The `st.chat_message` method is used to display both user and bot messages in the chat interface.

#### **Error Handling:**
- The `get_bot_response()` function handles errors in server communication and provides an error message if the bot fails to respond properly.

This script creates a chatbot interface that interacts with a locally running Rasa server, receives and sends messages, and displays both user and bot messages in a continuous chat history.

*Name2 worked on the merging of Rasa and Streamlit.*

### ChatBot Implementation with Rasa
#### 1. NLU (Natural Language Understanding)
- **Purpose**: Interprets user input (e.g., "I feel unwell").
- **Example**: 
  - **Intent**: What the user wants (e.g., "Report Illness").
  - **Entities**: Key details (e.g., "unwell").

#### 2. Rules
- **Purpose**: Define actions for specific situations.
- **Example**: 
  - If the user says "Hello", respond with a greeting.

#### 3. Stories
- **Purpose**: Define conversational flow.
- **Example**:
  - User: "Hi"
  - Bot: "Hello, how can I assist you today?"
  - User: "I feel unwell"
  - Bot: "Sorry to hear that, can you describe your symptoms?"

#### 4. Actions
Purpose of Actions in Rasa:
- **Interact with external systems**: Call APIs, query databases, or run models.
- **Manage conversation flow**: Determine next steps, ask questions, and provide responses.
- **Handle complex logic**: Define custom logic based on user inputs or conditions.

##### 1. ActionProvideTips
- **Purpose**: Provides personalized health tips based on user input.
- **How it works**:
  - Retrieves user's health conditions (e.g., smoking history, hypertension, heart disease).
  - Gives general tips (e.g., exercise, hydration).
  - Adds personalized tips based on health conditions.
- **Message**: Sends a message with relevant tips to the user.

##### 2. ActionPredictDiabetes
- **Purpose**: Predicts diabetes risk based on user inputs.
- **How it works**:
  - Retrieves user data (e.g., age, BMI, glucose levels).
  - Normalizes inputs and calculates prediction using a machine learning model.
  - Sends a message with the risk level (low, moderate, high) and recommendations.

##### 3. ActionRememberName
- **Purpose**: Remembers the user's name.
- **How it works**:
  - Extracts the user's name from the input.
  - Sets the name in a slot to remember for later use.
  - If no name is detected, asks the user to repeat it.
 
*Name2 handled the prediction part, and Name1 worked on the tips part.*
## Work done

### Name2 
- Collected the dataset.  
- Handled dataset transformation and description.  
- Performed dataset analysis and handled outliers.  
- Added realistic fake data and documented its effects.  
- Created and documented sample dialogs for chatbot use cases.  
- Recorded a video/screencast of the project.  

### Name1
- Developed the multi-page Web App using Streamlit.  
- Described 3 personas in the Wiki.  
- Identified and documented 5 use cases for the application.  
- Added input widgets to the application.  
- Applied two Scikit-Learn model training algorithms and documented the best fit.  
- Created the system persona for the chatbot.  
- Designed and documented the high-level dialog flow for chatbot use cases.  

### Both  
- Handled all documentation, including:  
  - The `requirements.txt` file.  
  - The `README.md` file.  
  - The Wiki.
- Developed the chatbot using Rasa.