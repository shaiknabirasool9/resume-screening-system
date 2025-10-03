import os

def read_resumes(resume_folder):
    """
    Reads all resumes from the given folder.
    Returns a dictionary: {filename: text_content}
    """
    resumes = {}
    for file in os.listdir(resume_folder):
        if file.endswith(".txt") or file.endswith(".pdf"):
            file_path = os.path.join(resume_folder, file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                resumes[file] = f.read()
    return resumes
