import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

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
