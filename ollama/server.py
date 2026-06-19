from fastapi import FastAPI, Body
 

from ollama import Client

app=FastAPI()


client=Client(
    host="http://localhost:11434",
)

@app.post("/chat")
def chat(
        messages:str= Body(..., description="The messages")
):
    response=client.chat(model="gemma:2b",messages=[
        {"role":"user", "content":messages}
    ])

    return {"response":response.message.content}
    