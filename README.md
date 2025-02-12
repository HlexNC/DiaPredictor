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

### Outliers
The handling of outliers was added in: https://github.com/FaresM7/DiaPredictor/-/wikis/Description-of-Differences-of-the-Original-Dataset-and-Final-Dataset

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

## Implementation of the Requests
### **Part 1: Project Setup**
1. **Multi-Page Streamlit Web App**:  
   We developed a multi-page app using Streamlit, allowing users to navigate between pages displaying data analysis, model predictions, and chatbot interactions.

2. **GitHub Repository & Wiki**:  
   All source code and documentation, including personas and use cases, were stored in a GitHub repository, with detailed explanations in the Wiki.

3. **Personas in Wiki**:  
   Three personas were created to represent different user types, each with specific goals, demographics, and challenges to help guide the app's development and user interface design.
- Personas in the wiki: https://github.com/FaresM7/DiaPredictor/-/wikis/Users-and-system-personas

4. **Use Cases**:  
   We identified five use cases that address key user tasks, such as feature manipulation and chatbot interaction for predictions.
- Use cases: https://github.com/FaresM7/DiaPredictor/-/wikis/Use-case

5. **`requirements.txt`**:  
   A `requirements.txt` file was generated to list all Python dependencies, ensuring easy setup and installation of necessary libraries for the project.

6. **`README.md`**:  
   A comprehensive `README.md` was created to explain the project’s functionality, setup instructions, and usage, providing clear guidance for users and developers.

7. **`venv` Virtual Environment**:  
   A virtual environment (`venv`) was set up to isolate dependencies and maintain consistency across different development setups.

8. **Free Data Source**:  
   We used a free diabetes dataset from Kaggle, ensuring it was publicly available and met the project’s requirements. Its link is mentioned in the Data chapter.

9. **Data Import (CSV)**:  
   The dataset was imported in CSV format, ensuring compatibility with the application and its analysis features.

10. **Data Analysis in Streamlit**:  
    The data was analyzed using Pandas within Streamlit, providing users with insights such as correlations, min/max values, and summary statistics visualized in charts.

11. **Data Description in Wiki**:  
    The data and its features were thoroughly described in the Wiki, including basic statistics, transformations, and the target variable.

 - Data Description: https://github.com/FaresM7/DiaPredictor/-/wikis/Dataset-Description

12. **Outlier Identification & Update**:  
    Outliers were identified using statistical methods, and we applied appropriate transformations or removals to ensure clean data for analysis.

 - Outlier Handling: https://github.com/FaresM7/DiaPredictor/-/wikis/Description-of-Differences-of-the-Original-Dataset-and-Final-Dataset

13. **Data Transformation**:  
    The dataset was transformed to ensure all variables were numerical and suitable for machine learning models, following best practices for data preprocessing.

 - Data Transformation: https://github.com/FaresM7/DiaPredictor/-/wikis/Dataset-Description

14. **Fake Data Generation**:  
    Realistic fake data was generated to enhance the model’s robustness, and its influence on training and predictions was explained in the Wiki.

15. **Input Widgets**:  
    We added interactive widgets (e.g., sliders, text inputs) in the Streamlit Diabetes Prediction page to allow users to change feature variables and observe how it affects the predictions.

16. **Model Training with Scikit-Learn**:  
    We implemented two Scikit-learn algorithms, Linear Regression and Decision Trees, to predict diabetes outcomes, and discussed their suitability in the Wiki.

17. **Use Case Fit for Chatbot**:  
    Two use cases (prediction and tips) were selected and discussed in the Wiki where the chatbot enhances user experience by answering queries and guiding them through predictions.
   - Use cases: https://github.com/FaresM7/DiaPredictor/-/wikis/ChatBot-Use-Cases


18. **System Persona for Chatbot**:  
    A system persona was defined for the chatbot, outlining its role, tone, and behavior to ensure effective communication with users. It can be found in the personas page in the Wiki.

19. **Sample Dialogs for Chatbot**:  
    We created three sample dialog flows for each use case, demonstrating how the chatbot would interact with users.
   - Sample dialogs: https://github.com/FaresM7/DiaPredictor/-/wikis/Dialogs

20. **Dialog Flow**:  
    A high-level dialog flow was designed to guide user interactions with the chatbot, ensuring smooth and intuitive conversations.
 - Dialogue Flow: https://github.com/FaresM7/DiaPredictor/-/wikis/Dialog-flow

### **Part 2: Implementation of Chatbot**
21. **Rasa Chatbot Implementation**:  
    A Rasa chatbot was developed to handle user queries and assist in predictions, with its configuration and source files added to the repository.
 - In-Depth Code Description: https://github.com/FaresM7/DiaPredictor/-/wikis/Code-Explanation

22. **Screencast of Project**:  
    A video was created showcasing the app’s features, including data analysis and chatbot interactions, and uploaded to the repository for demonstration. It is uploaded with the other files in the repository.

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
