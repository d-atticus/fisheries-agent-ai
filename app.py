
from fastapi import FastAPI
from agent.fisheries_agent import run_agent

app = FastAPI()

@app.get("/")
def home():

    return {"message":"Fisheries AI Agent running"}

@app.post("/chat")

def chat(data:dict):

    question = data["message"]

    answer = run_agent(question)

    return {"response":answer}
