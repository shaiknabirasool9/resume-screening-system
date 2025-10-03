import streamlit as st
from preprocessing import read_resumes
from job_matcher import match_resume_to_job
import os

st.title("Resume Screening System")

# Upload resumes folder
resume_folder = st.text_input("Enter path to resumes folder (e.g., data/resumes)")
job_description = st.text_area("Paste Job Description here")

if st.button("Match Resumes") and resume_folder and job_description:
    resumes = read_resumes(resume_folder)
    st.write(f"Found {len(resumes)} resumes.")
    
    for filename, text in resumes.items():
        match_percent, matched_skills = match_resume_to_job(text, job_description)
        st.write(f"**{filename}** → Match: {match_percent}% | Skills matched: {matched_skills}")
#"print('Hello, Resume Screening System!')" 
