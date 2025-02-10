# tasks/job_advising_task.py
from crewai import Task
from agents.job_advisor_agents import advisor_agent
from tools.job_advisor import generate_job_advice

def generate_advice_task(matched_jobs):
    job_advice = generate_job_advice(matched_jobs)  # Generating career advice
    return job_advice

job_advising_task = Task(
    agent=advisor_agent,
    expected_output="Generates career advice based on matched job postings, offering suggestions on skills to improve, CV optimizations, and targeted career paths.",
    description="Generate career advice based on the matched job postings.",
    run_function=generate_advice_task
)
