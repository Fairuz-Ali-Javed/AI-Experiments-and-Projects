import os
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
model = "openai/gpt-oss-120b"
client = Groq(api_key=api_key)



knowledge_base = {
    "tatto": "Has a tatto of dolphin shape in right hand",
    "favorite food": "loves curry"
}

def retrieve(question):
    if "tatto" in question:
        return knowledge_base["tatto"]
    elif "favorite food" in question:
        return knowledge_base["favorite food"]
    return None

sys_prompt = f"""
Answer within 50 tokens.
Use this information ONLY to give the answers = {knowledge_base}
"""
system_message = {
    "role": "system",
    "content": sys_prompt
}

def ask(question):
    message = {
        "role": "user",
        "content": question
    }
    messages = [system_message, message]

    response = client.chat.completions.create(model=model, messages = messages)
    return response.choices[0].message.content

# question = "Which brand tatto does sam altman have?"
# question = "What is his age?"
# question = "What is his favorite food?"
question = "What does he consume for energy?"
print(ask(question))