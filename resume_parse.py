import fitz  
import pymupdf
import re
import docx
from typing import Any, Dict

def extract_text_from_pdf(file_path: str) -> str:
    doc = pymupdf   .open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def parse_resume(text: str) -> Dict[str, Any]:
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    full_text = "\n".join(cleaned_lines)

    # Name: Try first non-empty line, fallback to first line
    name = None
    if cleaned_lines:
        name_match = re.match(r'^[A-Z][a-zA-Z .-]+$', cleaned_lines[0])
        name = name_match.group(0) if name_match else cleaned_lines[0]

    # Email
    email = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', full_text)

    # Phone (support various formats)
    phone = re.search(r'(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}', full_text)

    # URLs
    github = re.search(r'https?://(www\.)?github\.com/[A-Za-z0-9_-]+', full_text)
    linkedin = re.search(r'https?://(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+', full_text)
    portfolio = re.search(r'https?://[^\s]+', full_text)

    # Address (simple heuristic: look for lines with numbers and street keywords)
    address = None
    for line in cleaned_lines[:5]:
        if re.search(r'\d+ .*(Street|St\.|Avenue|Ave\.|Road|Rd\.|Block|Sector)', line, re.IGNORECASE):
            address = line
            break

    # Objective/Summary
    summary = None
    for i, line in enumerate(cleaned_lines):
        if "Objective" in line or "Summary" in line:
            summary = cleaned_lines[i+1] if i+1 < len(cleaned_lines) else None
            break

    # Skills: Look for lines containing 'Skill', 'Technical', 'Programming', etc.
    skills = []
    for line in cleaned_lines:
        if re.search(r'(Skill|Technical|Programming|Languages|Framework|Platform|Tool)', line, re.IGNORECASE):
            skills.extend([s.strip() for s in re.split(r'[:,]', line) if s.strip() and not re.search(r'(Skill|Technical|Programming|Languages|Framework|Platform|Tool)', s, re.IGNORECASE)])

    # Experience
    experience = []
    exp_pattern = re.compile(r'(Intern|Engineer|Developer|Manager|Analyst|Consultant|Project|Experience|Worked|Company)', re.IGNORECASE)
    for line in cleaned_lines:
        if exp_pattern.search(line):
            experience.append(line)

    # Education
    education = []
    edu_pattern = re.compile(r"(Bachelor|Master|PhD|High School|B\.Tech|M\.Tech|Diploma|Ph\.D|Degree|University|College)", re.IGNORECASE)
    for line in cleaned_lines:
        if edu_pattern.search(line):
            education.append(line)

    # Certifications
    certifications = []
    cert_pattern = re.compile(r"(Certification|Certified|Course|Training)", re.IGNORECASE)
    for line in cleaned_lines:
        if cert_pattern.search(line):
            certifications.append(line)

    # Projects
    projects = []
    proj_pattern = re.compile(r"(Project|Assignment|Research)", re.IGNORECASE)
    for line in cleaned_lines:
        if proj_pattern.search(line):
            projects.append(line)

    return {
        "name": name,
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None,
        "address": address,
        "summary": summary,
        "github": github.group(0) if github else None,
        "linkedin": linkedin.group(0) if linkedin else None,
        "portfolio": portfolio.group(0) if portfolio else None,
        "skills": skills if skills else None,
        "experience": experience if experience else None,
        "education": education if education else None,
        "certifications": certifications if certifications else None,
        "projects": projects if projects else None
    }

def extract_resume_data(file_path: str) -> Dict[str, Any]:
    if file_path.lower().endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .pdf or .docx file.")
    return parse_resume(text)