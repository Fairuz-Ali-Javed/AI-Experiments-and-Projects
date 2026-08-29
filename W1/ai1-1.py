import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
prompt = "What is the name of the tallest building in the world?"

message = {
    "role": role,
    "content": prompt
}

messages = [message]

response = client.chat.completions.create(model = model, messages = messages)

answer = response.choices[0].message.content
print(answer)