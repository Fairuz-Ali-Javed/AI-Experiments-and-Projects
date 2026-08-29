import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
prompt = "Give me a name for my clothing brand in one word. Give 10 names."

#System Message/Role Assignment
sys_message = {
    "role": "system",
    "content": "You are a creative designer with more than 50 years of experience and have mastered the craft of designing and creative thinking."
}


#Real message
message = {
    "role": role,
    "content": prompt
}

messages = [sys_message, message]

response = client.chat.completions.create(model = model, messages = messages, temperature = 2)
answer = response.choices[0].message.content
print(answer)
