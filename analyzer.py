import pandas as pd


def analyze_resume(text, job_description=""):

    text_lower = text.lower()
    jd_lower = job_description.lower()

    skills = [
        "python",
        "java",
        "html",
        "css",
        "javascript",
        "sql",
        "machine learning",
        "data science",
        "react",
        "node.js",
        "digital theory",
        "agentic ai"
    ]

    found_skills = []

    for skill in skills:
        if skill in text_lower:
            found_skills.append(skill)

    # Detect links
    github_present = "github.com" in text_lower
    linkedin_present = "linkedin.com" in text_lower

    # Detect experience
    experience_present = any(word in text_lower for word in
                             ["experience", "internship", "worked"])

    # Job Description Match
    jd_words = set(jd_lower.split())
    resume_words = set(text_lower.split())

    if len(jd_words) > 0:
        matched_words = jd_words.intersection(resume_words)
        jd_match = int((len(matched_words) / len(jd_words)) * 100)
    else:
        jd_match = 0

    # Score Calculation
    score = 0
    score += len(found_skills) * 5

    if "project" in text_lower:
        score += 15

    if experience_present:
        score += 15

    if "education" in text_lower:
        score += 10

    if github_present:
        score += 10

    if linkedin_present:
        score += 10

    score += jd_match // 4

    score = min(score, 100)

    # Suggestions
    suggestions = []

    if len(found_skills) < 5:
        suggestions.append("Add more technical skills")

    if not github_present:
        suggestions.append("Add GitHub profile link")

    if not linkedin_present:
        suggestions.append("Add LinkedIn profile link")

    if not experience_present:
        suggestions.append("Add experience/internship section")

    if "project" not in text_lower:
        suggestions.append("Add project section")

    if jd_match < 50:
        suggestions.append("Resume should match job description better")

    # Skill Frequency Chart
    skill_count = {}

    for skill in found_skills:
        skill_count[skill] = text_lower.count(skill)

    chart = pd.DataFrame({"Count": skill_count})

    return {
        "score": score,
        "skills": found_skills,
        "github": github_present,
        "linkedin": linkedin_present,
        "experience": experience_present,
        "jd_match": jd_match,
        "suggestions": suggestions,
        "chart": chart
    }