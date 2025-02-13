<p align="center">
  <a href="https://github.com/FaresM7/DiaPredictor">
    <img src="https://img.shields.io/badge/GitHub-Diapredictor-blue?style=flat-square&logo=github" alt="GitHub Badge">
  </a>
  <a href="https://www.python.org/downloads/release/python-310/">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white" alt="Requires Python 3.10+">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="MIT license badge">
  </a>
</p>

<h4 align="center">
Project DiaPredictor is a comprehensive web application—originally developed as a university project—designed to help individuals assess their diabetes risk and receive personalized recommendations. It leverages data analysis, machine learning, and a conversational chatbot interface to provide actionable health insights.
</h4>

---

## Table of Contents

- [Project Description](#project-description)
- [Screenshots](#screenshots)
- [Key Features](#key-features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps to Get Started](#steps-to-get-started)
  - [Training the Rasa Chatbot (Optional)](#training-the-rasa-chatbot-optional)
- [Data Overview](#data-overview)
  - [Dataset](#dataset)
  - [Data Handling and Augmentation](#data-handling-and-augmentation)
- [Usage](#usage)
  - [Personalized Stroke Risk Assessment](#personalized-stroke-risk-assessment)
  - [Interactive Data Analysis](#interactive-data-analysis)
  - [Chatbot Assistance](#chatbot-assistance)
- [Project Structure](#project-structure)
- [Disclaimer](#disclaimer)
- [Repository Visualization](#repository-visualization)
- [License](#license)
- [Contact](#contact)

---
## Project Description

**Diapredictor** provides an easy-to-use interface for individuals to assess their diabetes risk. The system is built on a robust dataset that has been cleaned and enriched with synthetic data to improve model accuracy.

The project features include:

- **Original vs. Modified Dataset Comparison**: View and analyze the differences between raw and enriched data.
- **Machine Learning Model Evaluation**: Compare performance metrics between models trained on different datasets.
- **Chatbot Assistant**: Receive personalized health advice and diabetes risk assessments.
- **Predictor System**: Input your health data and receive an immediate risk analysis.

The system is implemented using:

- **Streamlit** for an interactive frontend.
-**Scikit-Learn** for training and evaluating models.
- **Rasa** for an AI-powered chatbot.

## Screenshots

## Key Features

1. **Diabetes Risk Prediction**  
   - Users can input personal health metrics (e.g., age, BMI, glucose levels, smoking status).  
   - The model predicts the likelihood of diabetes and provides actionable health recommendations.  

2. **Comparative Model Analysis**  
   - Evaluate different models trained on both the original and enriched datasets.  
   - Metrics include **accuracy**, **precision**, **mean squared error (MSE)**, and **R² score**.  

3. **Chatbot Assistance**  
   - AI-powered chatbot offers real-time insights on diabetes risk, prevention, and lifestyle changes.  

4. **Data Preprocessing & Augmentation**  
   - **Imbalanced dataset?** We applied **SMOTENC** to generate synthetic minority class samples.  
   - Features like **gender, smoking history, and outliers** were handled for optimal model training.  

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

> [!NOTE]
> This dataset is used strictly for educational and demonstration purposes.


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
