# tasks/job_tasks.py

from tasks.cv_extraction_task import cv_extraction_task
from tasks.job_scraping_task import job_scraping_task
from tasks.job_matching_task import job_matching_task
from tasks.job_advising_task import job_advising_task

# List of tasks that will be used by CrewAI
tasks = [
    cv_extraction_task,        # Task for CV extraction
    job_scraping_task,         # Task for job scraping
    job_matching_task,         # Task for job matching
    job_advising_task          # Task for job advising
]
