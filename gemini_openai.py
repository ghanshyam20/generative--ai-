from openai import OpenAI
import os 
import dotenv

dotenv.load_dotenv()


client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Explain how AI works in a simple way."}
    ]
)


print(response.choices[0].message.content)


