# READ THE RESUME

myfile = open(r"D:\AI Engineer\Resume.txt", 'r')
myfile_content = myfile.read()
# print(content)
myfile.close()


# CREATE THE RESUME PARSER MODEL

import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-120b"

class ResumeEval(BaseModel):
    name: str
    email: str
    phone_no: int
    address: str
    education: str
    intership: str
    skills: str
    addition_skills: str
    projects: str
    collaboration: str
    open_source: str

schema = ResumeEval.model_json_schema()
sys_message = f"Read the content and take out personal information. Give the output in the form of JSON {schema}"
response_format = {
    "type": "json_object"
}


system_message = {
    "role": "system",
    "content": sys_message
}

msg = myfile_content
message = {
    "role": "user",
    "content": msg
}

messages = [system_message, message]
response = client.chat.completions.create(model = model, messages = messages, response_format = response_format)
ans = response.choices[0].message.content



# MATCH THE RESUME WITH THE JD
myfile2 = open(r"D:\AI Engineer\JD.txt", 'r')
jd = myfile2.read()
myfile2.close()

msg0 = f"""
You are a HR Manager with more than 20 years of experience. Below given is the 
Job Description for the role. You will be given the parsed resume in JSON format. Analyze and 
give a percentage of how well does the resume allign with the Job Description.

{jd}
"""
message0 = {
    "role": "user", 
    "content": msg0
}

message1 = {
    "role": "user",
    "content": ans
}

messages = [message0, message1]
response = client.chat.completions.create(model = model, messages = messages)
print(response.choices[0].message.content)


