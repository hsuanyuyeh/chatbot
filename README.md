A LLama3 based chatbot, fastapi served as the backend server, sending query to ollama prompt. Streamlit introduces the chatbot UI, storing the chat history.\
\
Run the backend server: uvicorn server:app --host 0.0.0.0 --port 8000\
Run the chatbot ui: streamlit run client_2.py
\
\
Backend: \
![screenshot](https://github.com/hsuanyuyeh/chatbot/blob/main/image_backend.png)
\
\
Chatbot UI: \
![screenshot](https://github.com/hsuanyuyeh/chatbot/blob/main/image_ui.png)
