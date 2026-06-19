# zero short promting 
# This is  just giving direct instructions 


from openai import OpenAI
import os 
import dotenv

dotenv.load_dotenv()


client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="you should only and only ans the wild animals related questions. Do not ans anything else ,Your name is Alexa. If user asks something other than wild animals , just say sorry   "
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, I am Ghan ! can you give me code to add numbers in js ??."}
    ]
)


print(response.choices[0].message.content)


