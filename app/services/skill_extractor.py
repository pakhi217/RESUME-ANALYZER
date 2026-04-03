# Simple keyword-based extraction

SKILLS_DB = [
    "python", "java", "c++", "machine learning", "deep learning",
    "flask", "django", "react", "sql", "mongodb", "data analysis"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))