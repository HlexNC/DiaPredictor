import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Additional_Scripts.normalizing_inputs_and_prediction import normalize_inputs

class ActionProvideTips(Action):
    def name(self) -> str:
        return "action_provide_tips"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Retrieve the slots
        age = tracker.get_slot("age")
        bmi = tracker.get_slot("bmi")
        smoking_history = tracker.get_slot("smoking_history")
        hypertension = tracker.get_slot("hypertension")
        heart_disease = tracker.get_slot("heart_disease")
        current_glucose = tracker.get_slot("current_glucose")
        
        tips = []

        # Randomize the glucose level tips
        if current_glucose > 180:
            tips.append(random.choice([
                "Your glucose levels are high. Consider reducing sugar intake, focusing on low-carb foods, and increasing fiber to help stabilize your levels. It’s essential to consult with your doctor about a management plan.",
                "With glucose levels above 180, it’s crucial to cut back on sugary foods and drinks. Focus on whole grains and leafy vegetables. Regular exercise can help stabilize your levels as well."
            ]))

        elif current_glucose > 140:
            tips.append(random.choice([
                "Your glucose levels are elevated. To help manage them, avoid sugary snacks and drinks, and consider regular physical activity such as walking or light jogging. Monitoring your glucose levels closely will help track progress.",
                "Elevated glucose levels can be managed with a balanced diet and regular exercise. Aim to limit high-sugar foods and increase fiber intake to stabilize your levels."
            ]))

        # Randomize BMI tips
        if bmi >= 30:
            tips.append(random.choice([
                "A BMI over 30 indicates a higher risk for complications. Incorporating regular physical activity, such as daily walks, and focusing on a balanced diet with fruits, vegetables, and lean proteins can help reduce your BMI. Small changes over time can make a big difference.",
                "With a BMI over 30, it’s important to start incorporating small changes. Begin by walking 30 minutes a day and incorporating more plant-based foods into your diet to improve your weight and health."
            ]))

        # Randomize heart disease tips
        if heart_disease:
            tips.append(random.choice([
                "Given your history of heart disease, it’s important to follow a heart-healthy diet that’s rich in omega-3 fatty acids, whole grains, and low in saturated fats. Regular exercise and managing stress levels will also contribute to better heart health.",
                "Since you have heart disease, focus on a diet rich in fruits, vegetables, and whole grains while limiting unhealthy fats. Regular cardiovascular exercise will also help support heart health."
            ]))

        # Randomize hypertension tips
        if hypertension:
            tips.append(random.choice([
                "Managing hypertension is critical. Focus on reducing salt intake, avoid processed foods, and engage in stress-relieving activities like yoga or meditation. Keeping your blood pressure under control will help reduce the strain on your heart.",
                "To manage hypertension, reduce salt intake and avoid high-sodium foods. Regular exercise like walking and relaxing activities like meditation will help keep your blood pressure in check."
            ]))

        # Randomize smoking history tips
        if smoking_history == "Current":
            tips.append(random.choice([
                "Smoking has a negative impact on both your heart and lung health. Consider seeking support to quit smoking, whether through counseling, nicotine replacement therapy, or a support group. Quitting smoking will improve your circulation and overall well-being.",
                "Since you're a current smoker, consider seeking help to quit. Smoking cessation will improve circulation, reduce your risk of heart disease, and benefit your overall health."
            ]))

        # Send back all of the tips based on the user information #
        dispatcher.utter_message("\n".join(tips))

        return []
    
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

class ActionProvideMissingData(Action):
    def name(self) -> str:
        return "action_provide_missing_data"

    def run(self, dispatcher, tracker, domain):
        missing_data = []

        # Check for each slot, and if missing, add it to the list
        if not tracker.get_slot("age"):
            missing_data.append("age")
        if not tracker.get_slot("hypertension"):
            missing_data.append("hypertension")
        if not tracker.get_slot("heart_disease"):
            missing_data.append("heart_disease")
        if not tracker.get_slot("bmi"):
            missing_data.append("bmi")
        if not tracker.get_slot("average_glucose"):
            missing_data.append("average_glucose")
        if not tracker.get_slot("current_glucose"):
            missing_data.append("current_glucose")
        if not tracker.get_slot("smoking_history"):
            missing_data.append("smoking_history")

        if missing_data:
            # If any data is missing, prompt the user for each one
            message = "I need the following information to proceed: "
            message += ", ".join(missing_data)
            dispatcher.utter_message(message)

class ActionRepeatMessage(Action):
    def name(self):
        return "action_repeat_message"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Please respond only with one of the provided possible answers.")
        return []
    
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



