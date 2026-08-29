import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-120b"
role = "user"

prompt1 = "Hi"
prompt2 = "What is the meaning of computer science?"
prompt3 = "Write an essay on theory of relativity in 1000 words"
prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]
    response = client.chat.completions.create(model = model, messages = messages, max_tokens = 200)
    # print(response.choices[0].message.content)

    #If reason for stopping is 'stop' means full message otherwise it reached the tokens limit
    print(f"prompt = {prompt} \n Input Tokens used = {response.usage.prompt_tokens} \n Output Tokens used = {response.usage.completion_tokens} \n Total Tokens used = {response.usage.total_tokens} \n Reason for stopping = {response.choices[0].finish_reason}")