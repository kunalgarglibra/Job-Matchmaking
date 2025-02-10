# tasks/cv_extraction_task.py
from crewai import Task
from agents.cv_extractor_agent import cv_extractor_agent
from tools.cv_extractor import extract_cv_data

def get_cv_data_from_user():
    cv_pdf_path = input("Please upload your CV (provide the file path): ")
    cv_data = extract_cv_data(cv_pdf_path)
    return cv_data

cv_extraction_task = Task(
    agent=cv_extractor_agent,
    expected_output="Extracts structured data such as name, skills, experience, education, and contact information from the user's CV PDF file.",
    description="Extract structured data (skills, experience, education) from the user's uploaded CV PDF.",
    run_function=get_cv_data_from_user
)
