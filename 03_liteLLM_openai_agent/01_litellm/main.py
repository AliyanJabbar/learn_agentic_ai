from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv() #loading environment variables from .env file

    
messages = [{"content":"what is Pakistan?","role":"user"}]
# def openai():
#     response = completion(
#         model="openai/gpt-4o",
#         messages=messages,
#         api_key=os.getenv("OPENAI_API_KEY")
#     )

#     print(response)
# openai() #won't work because paid even we have api but not tokens!

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=messages,
        api_key=os.getenv("GOOGLE_STUDIO_API_KEY")
    )

    print(response)
# gemini()

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=messages,      
        api_key=os.getenv("GOOGLE_STUDIO_API_KEY")
    )

    print(response['choices'][0]['message']['content'])
gemini2()