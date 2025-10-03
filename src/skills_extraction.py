import re

# Example list of skills
SKILLS_DB = ["Python", "SQL", "Machine Learning", "Data Analysis", "NLP", "Web Development"]

def extract_skills(text):
    """
    Extract skills from resume text by checking against SKILLS_DB
    """
    found_skills = []
    for skill in SKILLS_DB:
        pattern = re.compile(r"\b" + re.escape(skill) + r"\b", re.IGNORECASE)
        if pattern.search(text):
            found_skills.append(skill)
    return found_skills
