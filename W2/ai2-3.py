import os
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path
import time

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
model = "openai/gpt-oss-120b"
client = Groq(api_key = my_api_key)



def callLLM(systemprompt, userprompt):
    sys_message = {
        "role": "system",
        "content": systemprompt
    }

    message = {
        "role": "user",
        "content": userprompt
    }

    messages = [sys_message, message]
    response = client.chat.completions.create(model=model, messages = messages)
    return response.choices[0].message.content




def get_resume_skills(RESUME):
    sys_message = """
    You are a HR assistant.
    Your ONLY goal is to extract all the skills from the RESUME.
    You have to give the skills in a single line format where every skill is separated by a comma.    
    """

    message = f"""
    Here is a resume. Extract the skills from this resume.
    {RESUME}
    """

    return callLLM(sys_message, message)

def get_jd_skills(JD):
    sys_message = """
    You are a HR assistant.
    Your ONLY goal is to extract all the skills from the JD.
    You have to give the skills in a single line format where every skill is separated by a comma.    
    """
    message = f"""
    Here is a JD. Extract the skills from this JD.
    {JD}
    """

    return callLLM(sys_message, message)

def match_score(resumeskills, jdskills):
    sys_message = """
    You are a HR assistant.
    Your ONLY goal is to compare the skills from the resume and the jd
    and give a proper score based on the comparison. Also give a verdict within 100 words 
    on why you came to that decision. No fluff. Do not invent information.
    """

    message = f"""
    Here is the skills extracted from the resume and the jd.
    Please compare them and give me a score.

    JD Skills: {jdskills}
    RESUME Skills: {resumeskills}
    """

    return callLLM(sys_message, message)

RESUME = """
ARJUN PATEL
742 Evergreen Terrace, San Francisco, CA 94107 | (415) 555-0143 | arjun.patel.sde@email.com | linkedin.com/in/arjunpatelsde | github.com/arjunpatel

SUMMARY
Software Development Engineer with 5 years of experience building scalable backend services, distributed systems, and cloud-native applications. Proven track record of optimizing system performance, reducing latency, and leading technical initiatives in fast-paced engineering environments.

SKILLS

Programming Languages: Java, Python, Go, C++, TypeScript, SQL

System Design & Architecture: Microservices, Distributed Systems, RESTful APIs, gRPC, Event-Driven Architecture (Kafka, RabbitMQ)

Cloud & DevOps: AWS (Lambda, ECS, DynamoDB, S3), Docker, Kubernetes, Terraform, CI/CD Pipelines (GitHub Actions, Jenkins)

Databases & Caching: PostgreSQL, MySQL, Redis, MongoDB, Cassandra

Tools & Practices: Git, Linux, JUnit, Agile/Scrum, Test-Driven Development (TDD)

PROFESSIONAL EXPERIENCE

Software Development Engineer II
CloudScale Technologies — San Francisco, CA
July 2024 - Present

Designed and implemented high-throughput microservices using Go and Java, handling over 15 million daily requests with 99.99% uptime.

Migrated a legacy monolithic database layer to an event-driven architecture using Apache Kafka, reducing end-to-end transaction latency by 35%.

Spearheaded cost-optimization initiatives on AWS by rightsizing ECS clusters and implementing aggressive Redis caching policies, saving $45,000 annually.

Mentored junior engineers, conducted architectural code reviews, and enforced strict security and performance standards across engineering squads.

Software Development Engineer I
Vanguard Systems — San Jose, CA
August 2022 - June 2024

Developed core RESTful APIs and backend microservices using Java Spring Boot and PostgreSQL for a high-traffic fintech platform.

Optimized slow-running database queries and added strategic indexing, improving report generation speeds by nearly 50%.

Integrated automated CI/CD pipelines via GitHub Actions and Docker, cutting average deployment times from 45 minutes to under 8 minutes.

Participated in on-call rotations, diagnosing and resolving critical production incidents within defined SLAs.

Junior Software Engineer
ByteCraft Solutions — Seattle, WA
July 2021 - July 2022

Built and maintained responsive frontend components using TypeScript and React while contributing to backend Python/Django services.

Wrote comprehensive unit and integration tests using JUnit and PyTest, raising overall code test coverage from 62% to 88%.

Collaborated with product managers and QA engineers in Agile sprint cycles to deliver incremental feature updates.

EDUCATION

Bachelor of Science in Computer Engineering
University of California, Berkeley — Berkeley, CA
Graduated: May 2021
"""

JD1 = """
Job Title: Software Development Engineer (SDE)
Location: San Francisco, CA (Hybrid / Remote Options Available)
Department: Core Engineering
Employment Type: Full-Time

Position Overview
We are looking for a passionate and driven Software Development Engineer (SDE) to join our Core Engineering team. In this role, you will design, build, and scale high-performance distributed systems and backend services that power our next-generation platform. You will work closely with product managers, system architects, and cross-functional engineering teams to solve complex technical challenges and deliver robust solutions utilized by millions of users worldwide.

Key Responsibilities
Design & Develop: Build scalable, highly available, and low-latency microservices using modern programming languages (Java, Go, or Python).

System Architecture: Contribute to the architectural design of distributed systems, participating in technical design reviews and driving engineering best practices.

Performance & Optimization: Identify and resolve performance bottlenecks, optimize database queries, and ensure system reliability and high throughput under peak loads.

Collaboration: Partner with frontend engineers, product managers, and QA teams in an Agile/Scrum environment to deliver end-to-end features on time.

Code Quality & Testing: Write clean, maintainable code backed by comprehensive unit, integration, and performance tests; participate in rigorous peer code reviews.

Operations & Reliability: Take part in on-call rotations to troubleshoot, debug, and resolve production incidents swiftly, implementing root-cause analyses to prevent recurrence.

Qualifications & Requirements
Experience: 3 to 6 years of professional software development experience building scalable backend applications or distributed systems.

Technical Proficiency: Strong proficiency in at least one modern general-purpose programming language (Java, Go, C++, or Python).

Core CS Fundamentals: Solid foundation in data structures, algorithms, object-oriented programming, concurrency, and system design principles.

Databases & Storage: Hands-on experience with relational databases (PostgreSQL, MySQL) and caching or NoSQL technologies (Redis, DynamoDB, MongoDB).

Cloud & DevOps: Familiarity with cloud infrastructure (AWS, GCP, or Azure), containerization technologies (Docker, Kubernetes), and CI/CD pipelines.

Education: Bachelor's or Master's degree in Computer Science, Computer Engineering, or a related technical field (or equivalent practical experience).

Preferred Qualifications
Experience with event-driven architectures using messaging queues or streaming platforms (Apache Kafka, RabbitMQ).

Track record of optimizing cloud infrastructure costs and scaling systems to handle millions of daily active requests.
"""
    
JD2 = """
Job Title: Senior Backend & Distributed Systems Engineer
Location: San Francisco, CA (Hybrid)
Department: Engineering & Infrastructure
Employment Type: Full-Time

Position Overview
We are seeking a senior-level Software Development Engineer to join our infrastructure team to design, scale, and optimize high-throughput distributed systems. In this role, you will play a pivotal part in modernizing our architecture, transitioning monolithic structures to event-driven paradigms, and driving infrastructure cost-efficiency across our cloud ecosystem. You will work closely with other senior engineers and take a leadership role in mentoring junior talent and enforcing rigorous performance standards.

Key Responsibilities
System Architecture & Scaling: Design, develop, and maintain high-throughput microservices using Go and Java capable of handling massive daily traffic volumes with extreme reliability.

Event-Driven Migration: Lead initiatives to transition legacy database layers and synchronous architectures into decoupled, event-driven systems using Apache Kafka or similar messaging streams to minimize latency.

Cloud Infrastructure & Optimization: Manage and optimize cloud-native infrastructure on AWS (ECS, Lambda, S3, DynamoDB), implementing advanced caching strategies (Redis) and driving continuous cost-efficiency.

Technical Leadership & Mentorship: Conduct architectural code reviews, mentor junior and mid-level engineers, and champion engineering best practices, including TDD and CI/CD automation.

Reliability & Production Operations: Enforce strict uptime, security, and performance benchmarks; participate in incident management and drive root-cause analysis for production environments.

Qualifications & Requirements
Experience: 4 to 7 years of professional software engineering experience, with a strong focus on backend services, cloud infrastructure, and distributed architectures.

Programming Expertise: Deep hands-on proficiency in Go and Java, alongside strong foundations in Python, TypeScript, or C++.

Distributed Systems & Event-Driven Design: Proven production experience building microservices and working with event streaming platforms like Apache Kafka or RabbitMQ.

Cloud & DevOps Mastery: Extensive working knowledge of AWS cloud services, containerization (Docker, Kubernetes), Infrastructure as Code (Terraform), and automated CI/CD pipelines (GitHub Actions, Jenkins).

Data Management: Strong command of relational and NoSQL databases, including PostgreSQL, MySQL, Redis, and MongoDB, with a track record of query optimization.

Education: Bachelor's or Master's degree in Computer Science, Computer Engineering, or a related technical discipline.

Preferred Qualifications
Experience working in high-compliance or high-stakes fintech or enterprise SaaS environments.

Demonstrated history of leading cross-functional migration projects or infrastructure cost-reduction initiatives.

Open-source contributions or active technical leadership within the engineering community.
"""

#step1
r_skills = get_resume_skills(RESUME)
time.sleep(2)
#step2
jd_skills = get_jd_skills(JD2)
time.sleep(2)
#step3
score = match_score(r_skills, jd_skills)
print(score)





