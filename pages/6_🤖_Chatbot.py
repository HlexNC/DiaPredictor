import streamlit as st
import json
import requests
import time

def check_server_ready():
    rasa_url = "http://localhost:5005/status"
    while True:
        try:
            server_response = requests.get(rasa_url)
            if server_response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(5)

def get_bot_response(user_input):
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    try:
        payload = {"sender": "user", "message": user_input}
        response = requests.post(rasa_url, json=payload)
        response_json = response.json()
        
        # Handle multiple responses
        bot_responses = []
        if isinstance(response_json, list):
            for resp in response_json:
                if "text" in resp:
                    bot_responses.append(resp["text"])
        
        if not bot_responses:  # Handle empty responses
            bot_responses = ["Sorry, it seems there was an error when handling the response. Could you please repeat that?"]
            
        return bot_responses
        
    except requests.exceptions.RequestException as e:
        return [f"Error communicating with the bot: {e}"]

# Set up the page
st.set_page_config(page_title="Chatbot Interface", layout="wide")

with st.spinner("Loading DiaPreditor..."):
    server_response = check_server_ready()
    
if server_response:
    # Title and welcome message
    st.title("Chatbot Interface")
    st.markdown("Welcome to the chatbot! Type your messages below to start the conversation.")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat history
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input
    prompt = st.chat_input("Say something", key='user_input', max_chars=150)

    if prompt:
        # Add user message to chat
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get and display bot responses
        bot_responses = get_bot_response(prompt)
        
        # Add each bot response separately to the chat
        for response in bot_responses:
            st.session_state["messages"].append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)
