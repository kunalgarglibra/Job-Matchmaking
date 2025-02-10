# tasks/job_matching_task.py
from crewai import Task
from agents.job_matcher_agent import matcher_agent
from tools.job_matcher import match_jobs

def match_jobs_task(user_cv, job_postings):
    matched_jobs = match_jobs(user_cv, job_postings)  # Matching job postings with CV data
    return matched_jobs

job_matching_task = Task(
    agent=matcher_agent,
    expected_output="Matches the scraped job postings with the user's CV, identifying relevant jobs based on skills, experience, and other key CV elements. Returns matched jobs with a match score.",
    description="Match job postings with the user's CV data.",
    run_function=match_jobs_task
)
