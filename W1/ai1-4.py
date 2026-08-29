from pathlib import Path
import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()
my_apy_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key = my_apy_key)
model = "openai/gpt-oss-120b"

class Ticket(BaseModel):
    name: str
    email: str
    phone_no: int
    issue: str

schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}

sysmessage = f"Extract the personal information and necessary information precisely. Give in JSON Format. {schema}"
system_message = {
    "role": "system",
    "content": sysmessage
}

msg = """
Hello my name is Bob Marley and i recently purchases an iphone 14 pro max.
It has stopped working after 10 days. Because of this i m unable to call people and 
my work has stopped.
My phone number is 123456789. Regards Bob Marley email bm@gmail.com
"""
message = {
    "role": "user",
    "content": msg
}


messages = [system_message, message]
response = client.chat.completions.create(model= model, messages = messages, response_format = response_format)
ans = response.choices[0].message.content


import json
raw_json = ans
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.phone_no)
print(ticket.issue)
