# agents/job_matcher_agent.py
from crewai import Agent
from tools.job_matcher import match_jobs

matcher_agent = Agent(
    role="Job Matcher",
    goal="Identify the best job opportunities based on user preferences and skills.",
    backstory="An AI-powered job matching engine that connects job seekers with relevant jobs.",
    tools=[match_jobs],
    verbose=True
)
