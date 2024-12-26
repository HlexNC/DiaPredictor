import streamlit as st
import json
import requests

def get_bot_response(user_input):
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"

    try:
        payload = {"sender": "user", "message": user_input}
        response = requests.post(rasa_url, json=payload)
        response = json.dumps(response.json())
        response = json.loads(response)

        if isinstance(response, list) and response:  # Check if it's a non-empty list
                bot_response = response[0].get("text", "I didn't understand that.")
        else:  # Handle empty responses
            bot_response = "Sorry, it seems there was an error when handling the response. Could you please repeat that?"
    except requests.exceptions.RequestException as e:
        bot_response = f"Error communicating with the bot: {e}"

    return bot_response

# Set up the page
st.set_page_config(page_title="Chatbot Interface", layout="wide")

# Title and welcome message
st.title("Chatbot Interface")
st.markdown("Welcome to the chatbot! Type your messages below to start the conversation.")

# Placeholder for the chat history
chat_placeholder = st.empty()  # This is where we'll render the chat history

# A list to keep track of chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []


for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
prompt = st.chat_input("Say something", key='user_input', max_chars=150)

# Add a button to send the message
if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    bot_response = get_bot_response(prompt)    # send message to bot

    # Bot Response
    st.session_state["messages"].append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
        


