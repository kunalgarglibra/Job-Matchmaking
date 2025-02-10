# agents/cv_extractor_agent.py
from crewai import Agent
from tools.cv_extractor import extract_cv_data

cv_extractor_agent = Agent(
    role="CV Extractor",
    goal="Extract structured information (skills, experience, education) from the user's CV PDF.",
    backstory="An AI agent designed to read and analyze a user's CV PDF, extracting important details to help in job matching.",
    tools=[extract_cv_data],
    verbose=True
)
