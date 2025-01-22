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