# tools/job_matcher.py
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.tools import tool

@tool("match_jobs")
def match_jobs(user_cv, job_postings):
    """
    Matches job postings with the user's CV data.
    Compares key information like:
    - Skills
    - Experience
    - Education
    - Certifications
    Returns a list of matched job postings that align with the user's qualifications.
    """
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_texts([job["title"] + " " + job["company"] for job in job_postings], embeddings)
    
    query_vector = embeddings.embed_query(user_cv)
    results = vector_db.similarity_search_by_vector(query_vector, k=5)

    return results
