import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SessionStarted, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Additional_Scripts.normalizing_inputs_and_prediction import normalize_inputs

# PROVIDE TIPS
class ActionProvideTips(Action):
    def name(self) -> Text:
        return "action_provide_tips"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get user's health conditions
        smoking_history = tracker.get_slot("smoking_history")
        has_hypertension = tracker.get_slot("hypertension")
        has_heart_disease = tracker.get_slot("heart_disease")
        
        # Basic general tips (keeping it short)
        general_tips = [
            "monitor your blood glucose levels regularly",
            "maintain a healthy diet rich in fiber and low in refined sugars",
            "exercise regularly - aim for at least 150 minutes per week",
            "get enough sleep (7-9 hours per night)",
            "stay hydrated"
        ]
        
        # Get smoking-specific tip
        if smoking_history == "current":
            smoking_tip = "sonsider joining a smoking cessation program - quitting can help manage blood sugar"
        elif smoking_history == "former":
            smoking_tip = "great job quitting! Stay committed to your smoke-free status"
        else:  # never
            smoking_tip = "excellent choice staying smoke-free - this helps reduce diabetes risk"
            
        # Get hypertension tip if applicable
        hypertension_tip = (
            "keep your blood pressure in check with regular monitoring and reduced salt intake"
            if has_hypertension.lower() == "yes" else None
        )

        # Get heart disease tip if applicable
        heart_disease_tip = (
            "work closely with your doctor to manage both heart disease and diabetes risk"
            if has_heart_disease.lower() == "yes" else None
        )
        
        # Combine all tips into a single message
        message = "Here are some helpful tips for managing diabetes risk:\n\n"

        # Start the message with general tips
        message += "General Tips: "
        # Add the tips, separated by commas
        message += ", ".join(general_tips) + "."

        message += f"\n\nBased on your smoking history:\n {smoking_tip}"
        
        print(hypertension_tip, heart_disease_tip)
        if hypertension_tip:
            message += f"\n\nFor your hypertension:\n{hypertension_tip}"

        if heart_disease_tip:
            message += f"\n\nRegarding heart disease:\n{heart_disease_tip}"
        
        dispatcher.utter_message(text=message)
        return []
    
# PREDICTS DIABETES AND SENDS BACK RESULTS
class ActionPredictDiabetes(Action):
    def name(self) -> str:
        return "action_predict_diabetes"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Retrieve the slots
        age = tracker.get_slot("age")
        bmi = tracker.get_slot("bmi")
        smoking_history = tracker.get_slot("smoking_history")
        hypertension = tracker.get_slot("hypertension")
        heart_disease = tracker.get_slot("heart_disease")
        current_glucose = tracker.get_slot("current_glucose")
        average_glucose = tracker.get_slot("average_glucose")

        # Normalizes input values
        inputs = [[age, bmi, average_glucose, current_glucose]]

        # Prepare user input as a feature vector
        prediction = normalize_inputs(inputs, smoking_history, hypertension, heart_disease)

        if prediction < 0.3:
            dispatcher.utter_message("You are unlikely to have diabetes. Nonetheless, it’s always good to keep track of your health.")
        elif prediction < 0.7:
            dispatcher.utter_message("You have a moderate risk of diabetes. Consider adopting healthier lifestyle choices and monitor your health regularly.")
        else:
            dispatcher.utter_message("You have a high risk of diabetes. I strongly recommend consulting a doctor for further testing.")

# REMEMBER USER NAME
class ActionRememberName(Action):
    def name(self) -> Text:
        return "action_remember_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_name = next(tracker.get_latest_entity_values("name"), None)
        if user_name:
            return [SlotSet("name", user_name)]
        else:
            dispatcher.utter_message(text="I didn't quite catch your name. Could you repeat it?")
            return []

