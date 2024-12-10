A LLama3 based chatbot, fastapi is the backend server, sending query to ollama prompt where streamlit provides the chatbot UI.\
\
Run the backend server: uvicorn server:app --host 0.0.0.0 --port 8000\
Run the chatbot ui: streamlit run client_2.py\