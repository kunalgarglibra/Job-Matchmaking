# tools/job_advisor.py
from langchain.chat_models import ChatOpenAI
from langchain.tools import tool

@tool("generate_job_advice")
def generate_job_advice(job_list):
    """
    Analyzes the matched job postings and provides personalized career advice.
    The advice may include:
    - Career direction based on available job opportunities
    - Recommendations for skill improvement or upskilling
    - Suggestions on how to optimize the CV for better job matching
    Returns the advice as a string or a structured message.
    """
    llm = ChatOpenAI(model_name="gpt-4")
    prompt = f"Suggest the best jobs from this list based on skills and experience: {job_list}"
    advice = llm.predict(prompt)
    return advice
