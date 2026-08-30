import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import regex as re
import time

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
model = "openai/gpt-oss-120b"
client = Groq(api_key = my_api_key)


def get_price(product):
    if product == "Notebook":
        return "102$"
    elif product == "Pen":
        return "5$"
    else:
        return None

tools = {
    "get_price": get_price
}
sys_message = f"""
#ROLE: You are a product support assistant.

You have these tools at your disposal and none other nor can u use any other.
Your tools:
get_price(product_name)

IMPORTANT:
CALL THE TOOLS ONLY IN THIS FORMAT.

For example,
for getting the price of a notebook: get_price("Notebook")
for getting the price of a pen: get_price("Pen")

Never call like this:
get_price("noteBook")
get_price("pEn")
get_price(product = "Notebook")
get_price(product_name = "Notebook")


Follow These rules step by step:
1) Decide what you need FIRST.
2) Call ONLY ONE tool at a time.
3) After calling the tool WAIT/STOP IMMEDIATELY.
4) Never guess/invent or even give false information outside of the function.
5) Wait for your observation.
6) Then decide your next action.
7) When the task is complete give the final answer.
8) DO NOT REPLY WITH ANY OTHER FORMAT OTHER THAN THE GIVEN FORMAT.

Format To Follow When Performing A Task:

Thought: What action you are going to take right now.
Action: tool_name(argument)

When Finished Give the result ONLY in this format:

Final Answer: your final answer.


"""

system_message = {
    "role": "system",
    "content": sys_message
}

def run(question):
    message = {
        "role": "user",
        "content": question
    }

    messages = [system_message, message]

    for step in range(5):
        print(f"------STEP{step+1}------")

        response = client.chat.completions.create(model = model, messages = messages)
        answer = response.choices[0].message.content

        print(answer)

        if "Final Answer:" in answer:
            break


        match = re.search(r"Action:\s*(\w+)\((.*?)\)", answer)

        if match:
            tool_name = match.group(1)
            tool_input = match.group(2)
            tool_input = tool_input.strip()
            tool_input = tool_input.strip('"')

            if tool_name in tools:
                tool = tools[tool_name]
                observation = tool(tool_input)
            else:
                observation = "Tool not found"


            print("Observation:", observation)


            messages.append({
                "role": "assistant",
                "content": answer
            })
            messages.append({
                "role": "assistant",
                "content": f"Observation: {observation}"
            })
            time.sleep(5)

prompt = """
I want to buy a pen and a notebook. Give me the costs of both the objects please.
"""
run(prompt)
    