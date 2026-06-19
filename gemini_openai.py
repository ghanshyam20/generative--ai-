from openai import OpenAI
import os 
import dotenv

dotenv.load_dotenv()


client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# this is just free flaoting convo , but this way we generally dont do it ,
# now  this version is a bit strict that i have set background system prompt that it will only answer wild animals related question and if the question is not related to wild animals it will say 'I am sorry I can only answer wild animals related question'.

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":"You are an expert in wild animals and only  and only ans wild animals related question and you will never answer any other question."
        "if the query is not related to wild animals you will say 'I am sorry I can only answer wild animals related question'."},
        {"role": "user", "content": "Hey, I am Ghan ! can you give tell me wild boar in chitwan  to add numbers  ??."}
    ]
)


print(response.choices[0].message.content)


