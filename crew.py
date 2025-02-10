# crew.py
from crewai import Crew
from tasks.job_tasks import tasks
from tasks.cv_extraction_task import cv_extraction_task
from agents.job_scraper_agent import scraper_agent
from agents.job_matcher_agent import matcher_agent
from agents.job_advisor_agents import advisor_agent
from agents.cv_extractor_agent import cv_extractor_agent

crew = Crew(
    agents=[scraper_agent, matcher_agent, advisor_agent, cv_extractor_agent],
    tasks=tasks + [cv_extraction_task]
)

if __name__ == "__main__":
    crew.kickoff()
