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

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/FaresM7/DiaPredictor

2. Create a virtual environment with Python 3.10
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install the required dependencies
   ```bash
   pip install -r requirements.txt

4. Run the application
   ```bash
   python start.py

## Data
### Original dataset

We used the [Diabetes prediction dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) from Kaggle for training the models and later enhance the dataset.