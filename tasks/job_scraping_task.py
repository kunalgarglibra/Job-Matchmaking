# tasks/job_scraping_task.py
from crewai import Task
from agents.job_scraper_agent import scraper_agent
from tools.job_scraper import scrape_jobs

def scrape_jobs_task():
    job_postings = scrape_jobs()  # Scraping job postings
    return job_postings

job_scraping_task = Task(
    agent=scraper_agent,
    expected_output="Scrapes job postings from various online job portals and returns a list of jobs, including job title, company name, required skills, location, and job description.",
    description="Scrape job postings from various job portals.",
    run_function=scrape_jobs_task
)
