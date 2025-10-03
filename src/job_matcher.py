from skills_extraction import extract_skills

def match_resume_to_job(resume_text, job_description_text):
    """
    Compares resume skills to job description skills
    Returns match percentage
    """
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description_text))
    
    if not job_skills:
        return 0
    
    matched_skills = resume_skills.intersection(job_skills)
    match_percentage = len(matched_skills) / len(job_skills) * 100
    return round(match_percentage, 2), list(matched_skills)
