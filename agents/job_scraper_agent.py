# agents/job_scraper_agent.py
from crewai import Agent
from tools.job_scraper import scrape_jobs

scraper_agent = Agent(
    role="Job Scraper",
    goal="Extract job postings from various websites.",
    backstory="A highly experienced web scraper trained to collect job postings efficiently.",
    tools=[scrape_jobs],
    verbose=True
)
