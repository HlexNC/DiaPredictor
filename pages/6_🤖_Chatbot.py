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

# Check server readiness only once
if "server_ready" not in st.session_state:
    with st.spinner("Loading DiaPreditor..."):
        st.session_state["server_ready"] = check_server_ready()

if st.session_state["server_ready"]:
    # Title and welcome message
    st.title("Chatbot Interface")
    st.markdown("Welcome to the chatbot! Type your messages below to start the conversation.")

    # Placeholder for the chat history
    chat_placeholder = st.empty()  # This is where we'll render the chat history

    # A list to keep track of chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display previous chat messages
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input for user messages
    prompt = st.chat_input("Say something", key='user_input', max_chars=150)

    if prompt:
        # Add user message to chat history
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get bot response
        bot_response = get_bot_response(prompt)

        # Add bot response to chat history
        st.session_state["messages"].append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.markdown(bot_response)
