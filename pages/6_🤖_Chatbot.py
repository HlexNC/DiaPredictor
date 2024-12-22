import streamlit as st

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
        
    # Example bot response (you would replace this with a response from Rasa)
    bot_response = f"Bot: I see you said '{prompt}'."
    st.session_state["messages"].append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
        


