import streamlit as st
import requests

class Config:
    PAGE_TITLE = "Ollama Chatbot"
    OLLAMA_MODELS = ("llama3:latest")
    SERVER_IP_ADDRESS = "127.0.0.1"
    SERVER_PORT_NUMBER = 8000

server_ip_and_port = f"{Config.SERVER_IP_ADDRESS}:{Config.SERVER_PORT_NUMBER}"

st.set_page_config(
    page_title=Config.PAGE_TITLE,
    initial_sidebar_state="expanded"
)

st.title(Config.PAGE_TITLE)

with st.sidebar:
    st.markdown('# Chat Options')
    model = st.selectbox('What model would you like to use?', Config.OLLAMA_MODELS)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("What would you like to ask?"):
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    with st.spinner('Generating response...'):
        get_response = requests.get(f"http://{server_ip_and_port}/query/", params={'query': user_prompt})
        post_response = requests.post(f"http://{server_ip_and_port}/response/")
    
    with st.chat_message("assistant"):
        response_data = post_response.json()
        st.markdown(response_data)
    
    st.session_state.messages.append({"role": "assistant", "content": response_data})

