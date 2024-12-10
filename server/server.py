from fastapi import FastAPI
from langchain_ollama import OllamaLLM


app = FastAPI()
class OllamaResponse:
    def __init__(self, model_name=None):
        self.model_name = "llama3" if not model_name else model_name
        self.llm = OllamaLLM(model=self.model_name)
        self.query = None
        self.response = None
        self.chain = []

    def set_query(self, query):
        self.query=query
        self.chain.append({"role":  "user", "content": query})

    def get_response_from_ollama(self):
        if not len(self.chain) == 1:
            query = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.chain])
            self.response = self.llm.invoke(query)
        else:
            self.response = self.llm.invoke(self.query)
        self.chain.append({"role": "AI", "content": self.response})

chatbot = OllamaResponse()

@app.get("/query/")
def receive_query(query: str):
    chatbot.set_query(query)
    chatbot.get_response_from_ollama()

@app.post("/response/")
def send_response():
    return chatbot.response

if __name__ == "__main__":
    test_run = OllamaResponse()
    query = r"Hello! How are you?"

    test_run.set_query(query)
    test_run.get_response_from_ollama()

    print(test_run.response)
