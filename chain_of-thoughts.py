# CTO 
# Chain of thoughts prompting is a technique that it will think before ans 







import dotenv
from openai import OpenAI
import os 
import dotenv
import json

dotenv.load_dotenv()


client=OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="""
    you are an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN AND OUTPUT steps.
    you need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPOUT.

    Rules:
    - Strictly FOLLOW the given JSON output format.
    - Only run one step at a time 
    - The sequence of steps is START (where user gives an input) , PLAN (THAT CAN BE 
    multiple times) and finally OUTPUT (which is going to the displayed to the user
    )


    Output JSON Format:

    {{
    "step":"START: | "PLAN": | "OUTPUT", "content":"string"
    }}


    Example:
    Start:Hey, can you solve 2+3*5/10 
    PLAN: {"step":"PLAN": "content":"seems like user  is intrested 
    maths problem"}

    PLAN: {"step":"PLAN": "content": "looking at the problem, we should using this BODMAS method
      "}

    PLAN:{"step":"PLAN": "content": " yes, the BODMAS is correct thing to be done here"}

    PLAN: {"step":"PLAN": "content": "first we must multiply 3*5 which is 15"}

    PLAN: {"step": "PLAN": "content": " Now the new equations is 2+15/10"}

    PLAN: {"step":"PLAN": "content": "we must perform divide that is 15/10=1.5}"}
    PLAN:{"step":"PLAN": "content": "Now the new equation is 2+1.5"}
    PLAN:{"step":"PLAN": "content": "Now finally lets perform the addition 3.5  "}

    PLAN:{"step":"PLAN": "content": "Great, we have solved and finally left with 3.5 as ans"}


    OUTPUT:{"step": "OUTPUT":"content": "Great, we have solved and left with 3.5 as ans "}










"""


response=client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write a code to add n numbers in js ??"},

        # manually keep adding messages to history 
        {"role":"assistant", "content":json.dumps({"step":"START","content":"you want a js code to add 'n' numbers."})}
    ]
)


print(response.choices[0].message.content)
