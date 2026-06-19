# structure output few short promoting
# this is just a enhance version of few short prompting 
# where we can structure the output in specific manner or format




from openai import OpenAI
import os 
import dotenv

dotenv.load_dotenv()


client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="""you should only and only ans the wild animals related questions. Do not ans anything else ,Your name is Alexa. If user asks something other than wild animals , just say sorry.

    Rule:
    - Strictly follow the output in Json format 

    Output Format:

    {{
    "animal_name":"string" or NOne,
    "description":"string"}}




    Examples:
    Q: can you  explain about a+b  whole square ??
    A:{{ "code": None, "description": "I am sorry}}

    Q: can you tell me about chitwan national park ??
    A: Yes, Chitwan National Park is a protected area in Nepal known for its rich biodiversity, including Bengal tigers, one-horned rhinoceroses, and various bird species. It is a UNESCO World Heritage Site and a popular destination for wildlife enthusiasts and nature lovers.
  """
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, I am Ghan ! can you give me code to subtract two numbers is js  ??"}
    ]
)


print(response.choices[0].message.content)

# giving an exaples to the model to undestand the pattern of the question and answer and 
# then  it increases the accuracy 




