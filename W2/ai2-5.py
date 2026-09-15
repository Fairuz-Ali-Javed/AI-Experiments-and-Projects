import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()
api_key = os.getenv("GROQ_API")
model = "openai/gpt-oss-120b"
client = Groq(api_key=api_key)


aboutme = """
JAKE MERCER
San Francisco, CA | (555) 382-9104 | jake.mercer@email.com | linkedin.com/in/jakemercer | github.com/jake-dev

OBJECTIVE
Driven Computer Science undergraduate with a rigorous academic background and extensive hands-on project experience in modern web technologies and cloud databases. Eager to leverage strong technical skills in Python, TypeScript, and React to contribute effectively as a Software Engineering Intern.

EDUCATION
University of California, Berkeley — Berkeley, CA

Bachelor of Science in Computer Science | Expected Graduation: May 2027

Relevant Coursework: Data Structures & Algorithms, Computer Architecture, Database Systems, Software Engineering, Artificial Intelligence

Academic Honors: Dean's Honor List (Fall 2024, Spring 2025), UC Berkeley Regents Scholar

TECHNICAL SKILLS
Programming Languages: Python, JavaScript, TypeScript, Java, SQL, HTML5/CSS3

Frontend: React.js, Next.js, Tailwind CSS, Redux

Backend: Node.js, Express.js, FastAPI, RESTful APIs

Databases: PostgreSQL, MongoDB, Redis

Tools & Technologies: Git, GitHub, Docker, Postman, AWS (S3, EC2), Linux/Unix

PROJECTS
DevSync - Real-Time Collaborative Code Editor | TypeScript, React, Node.js, WebSockets, Docker

github.com/jake-dev/devsync | January 2026 - February 2026

Built a full-stack real-time code editor allowing multiple users to write, execute, and debug code simultaneously in a shared browser session.

Engineered secure WebSocket connections via Socket.io for instantaneous text synchronization with sub-50ms latency.

Containerized the application using Docker and deployed the backend microservice to AWS EC2 for high availability.

EcoTrack - Carbon Footprint Analytics Dashboard | Python, FastAPI, PostgreSQL, Chart.js, Tailwind CSS

github.com/jake-dev/ecotrack-analytics | October 2025 - November 2025

Developed a data-driven web dashboard that calculates user energy consumption and visualizes personal carbon metrics over time.

Designed complex SQL queries and relational database schemas in PostgreSQL to handle data ingestion from multiple external utility APIs.

Implemented clean RESTful endpoints using FastAPI with automated data validation powered by Pydantic.

EXTRACURRICULAR ACTIVITIES & LEADERSHIP
UC Berkeley Computer Science Society — Active Member & Hackathon Team Lead

August 2024 - Present

Participated in weekly algorithmic problem-solving workshops and peer code review sessions focusing on clean code principles.

Led a cross-functional team of 4 students to build an open-source campus navigation tool during the annual CalHacks event, placing in the top 10% out of 500+ competing teams.

CERTIFICATIONS
AWS Certified Cloud Practitioner — Amazon Web Services (December 2025)

The Complete JavaScript Bootcamp — Udemy (August 2024)

"""



sys_message = f"""
#ROLE: You are a support assistant.

#TASK: 
You are supposed to answer questions related to a person named "Jake".
This is the information about "Jake" given below:
About Jake: {aboutme}

#CONSTRAINTS:
DO NOT INVENT INFORMATION. BE COMPLETELY HONEST.
WHATEVER IS WRITTEN IN THE ABOUT ME OF "Jake" ONLY USING THAT YOU HAVE TO ANSWER.
Explain things professionally and keep it simple.
Keep the user hooked at all times.

#FALLBACK:
If the user answers for a question other than about "Jake" then reply with the text given below:
'I apologise but i m not made for answering such questions. Would you like to know anything else
about Jake?'
"""

system_message = {
    "role": "system",
    "content": sys_message
}
messages = [system_message]


def call_llm(userprompt):
    message = {
        "role": "user",
        "content": userprompt
    }
    messages.append(message)

    response = client.chat.completions.create(model=model, messages = messages)
    assistant_message = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }
    messages.append(assistant_message)

    return response.choices[0].message.content

while True:
    ask = input("Enter (type exit to leave):")
    if ask.lower() == "exit":
        break

    time.sleep(2)
    print(call_llm(ask))

    






