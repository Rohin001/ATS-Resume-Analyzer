import streamlit as st
from PyPDF2 import PdfReader
from analyzer import analyze_resume
from report import generate_report
from styles import apply_styles

st.set_page_config(
    page_title="ATS Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

apply_styles()

st.title("📄 ATS Resume Analyzer")
st.subheader("Upload your resume and get ATS analysis")

# Job Description Input
job_description = st.text_area(
    "Paste Job Description",
    height=150
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Analyze Resume
    results = analyze_resume(text, job_description)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("ATS Score", f"{results['score']}/100")

    with col2:
        st.metric("Skills Found", len(results["skills"]))

    with col3:
        st.metric("JD Match", f"{results['jd_match']}%")

    with col4:
        st.metric("Suggestions", len(results["suggestions"]))

    st.progress(results["score"] / 100)

    # Job Match Result
    st.subheader("Job Description Match")

    if results["jd_match"] >= 80:
        st.success(f"{results['jd_match']}% Match → Strong Resume Fit ✅")

    elif results["jd_match"] >= 50:
        st.warning(f"{results['jd_match']}% Match → Moderate Resume Fit")

    else:
        st.error(f"{results['jd_match']}% Match → Needs Improvement")

    left, right = st.columns(2)

    with left:
        st.subheader("Resume Text")
        st.text_area("", text, height=400)

    with right:
        st.subheader("Detected Skills")

        for skill in results["skills"]:
            st.success(skill)

        st.subheader("Profile Checks")

        st.write(
            f"GitHub: {'Present' if results['github'] else 'Missing'}"
        )
        st.write(
            f"LinkedIn: {'Present' if results['linkedin'] else 'Missing'}"
        )
        st.write(
            f"Experience: {'Present' if results['experience'] else 'Missing'}"
        )

        st.subheader("Suggestions")

        for suggestion in results["suggestions"]:
            st.warning(suggestion)

    st.subheader("Skill Frequency Chart")
    st.bar_chart(results["chart"])

    report = generate_report(results)

    st.download_button(
        "Download ATS Report",
        report,
        "ATS_Report.txt"
    )