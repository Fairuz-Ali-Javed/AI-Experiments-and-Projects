import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
model = "openai/gpt-oss-120b"
client = Groq(api_key = my_api_key)


def answers(msg):
    message = {
        "role": "user",
        "content": msg
    }
    messages = [message]
    response = client.chat.completions.create(model = model, messages = messages)
    return response.choices[0].message.content

prompt = """
#ROLE:
You are a mobile/laptop company assistant.

#TASK:
You need to classify the issue into a category.

#CONSTRAINT:
You have to classify the issue in either of the three categories ONLY -> Billing, Technical, Return

#OUTPUT FORMAT:
Your answer is ALWAYS supposed to only be in one word, i.e, only the categories mentioned.

#FALLBACK:
If the query is completely unrelated with the companies queries and doesnt come under the categories then reply with NONE.

This is a user complaint.
My chair is big
"""

print(answers(prompt))