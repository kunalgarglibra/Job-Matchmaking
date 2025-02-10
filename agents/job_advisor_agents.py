# agents/job_advisor_agent.py
from crewai import Agent
from tools.job_advisor import generate_job_advice

advisor_agent = Agent(
    role="Job Advisor",
    goal="Analyze job matches and suggest the best jobs for the user.",
    backstory="A career coach AI that provides expert job search advice.",
    tools=[generate_job_advice],
    verbose=True
)
