# tools/job_scraper.py
from bs4 import BeautifulSoup
import requests
from langchain.tools import tool

@tool("scrape_jobs")
def scrape_jobs():
    """
    Scrapes job postings from multiple job boards and returns a list of job postings.
    Each job posting contains details such as:
    - Job title
    - Company name
    - Job description
    - Required skills
    - Location
    - Date posted
    Returns a list of dictionaries, each representing a job posting.
    """
    url = "https://www.indeed.com/jobs?q=machine+learning&l=remote"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job_card in soup.find_all("div", class_="job_seen_beacon"):
        title = job_card.find("h2").text.strip()
        company = job_card.find("span", class_="companyName").text.strip()
        location = job_card.find("div", class_="companyLocation").text.strip()
        jobs.append({"title": title, "company": company, "location": location})

    return jobs
