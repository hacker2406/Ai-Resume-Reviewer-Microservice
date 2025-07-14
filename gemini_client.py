import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("GEMINI_API_KEY")

PROMPT_TEMPLATE=''' You are an experienced HR recruiter and career advisor

Analyze the following resume data and provide a detailed review of the candidate's qualifications, skills, and experiences.
Focus on the strengths, areas for improvement, and overall fit for a software engineering position. 


Resume Data: <insert resume data>
Provide your analysis in a structured format, highlighting key points and recommendations for the candidate's career development        

'''

def get_resume_reviews(resume_json:dict)->str:
    genai.configure(api_key=API_KEY)
    prompt=PROMPT_TEMPLATE.replace("<insert resume data>",str(resume_json))
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(prompt)
    return response.text

