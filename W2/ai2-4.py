import os
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

load_dotenv()

api_key = os.getenv('GROQ_API')
model = "openai/gpt-oss-120b"
client = Groq(api_key = api_key)


# prompt = "Explain quantum physics."
prompt = "Explain about the working of a cpu."

message = {
    "role": "user",
    "content": prompt
}
messages = [message]

#without streaming
# response = client.chat.completions.create(model=model, messages=messages, stream = False)
# print(response.choices[0].message.content)

#with steaming
response = client.chat.completions.create(model = model, messages = messages, stream = True)
for chunk in response:
    answer = chunk.choices[0].delta.content
    if answer:
        print(answer, end = "")
        # print(answer, end = "", flush = True)