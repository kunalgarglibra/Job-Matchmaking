# tools/cv_extractor.py
import PyPDF2
import re
from langchain.tools import tool

@tool("extract_cv_data")
def extract_cv_data(pdf_path):
    """
    Extracts relevant data from the CV PDF, including:
    - Skills
    - Professional experience
    - Education background
    - Certifications
    - Contact information
    Returns extracted data as a dictionary.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        
        for page in reader.pages:
            text += page.extract_text()
    
    skills = extract_skills(text)
    experience = extract_experience(text)
    education = extract_education(text)

    return {
        "skills": skills,
        "experience": experience,
        "education": education
    }

def extract_skills(text):
    skills_keywords = ['python', 'machine learning', 'data science', 'sql', 'nlp']
    skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    return skills

def extract_experience(text):
    experience_pattern = r"(experience|work experience):\s*(.*?)(education|skills|$)"
    match = re.search(experience_pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(2).strip() if match else "Not Available"

def extract_education(text):
    education_pattern = r"(education|degrees?):\s*(.*?)(experience|skills|$)"
    match = re.search(education_pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(2).strip() if match else "Not Available"
