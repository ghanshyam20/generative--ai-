# few short prompting 
# This is  a promot directly giving the instructions to the models and few examples to the models.
 


from openai import OpenAI
import os 
import dotenv

dotenv.load_dotenv()


client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="""you should only and only ans the wild animals related questions. Do not ans anything else ,Your name is Alexa. If user asks something other than wild animals , just say sorry.
    Examples:
    Q: can you  explain about a+b  whole square ??
    A: I am sorry i can only help with wild animals related question.

    Q: can you tell me about chitwan national park ??
    A: Yes, Chitwan National Park is a protected area in Nepal known for its rich biodiversity, including Bengal tigers, one-horned rhinoceroses, and various bird species. It is a UNESCO World Heritage Site and a popular destination for wildlife enthusiasts and nature lovers.
  """
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, I am Ghan ! can you explain me  types of tiger found in chitwan national park ??"}
    ]
)


print(response.choices[0].message.content)

# giving an exaples to the model to undestand the pattern of the question and answer and 
# then  it increases the accuracy 




