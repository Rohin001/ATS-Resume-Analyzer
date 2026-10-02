# 📄 ATS Resume Analyzer

ATS Resume Analyzer is a Python-based web application designed to analyze resumes and provide useful feedback based on **ATS (Applicant Tracking System)** criteria.

The application allows users to upload a PDF resume and enter a job description. It extracts the resume text, detects technical skills, checks important profile information, calculates a customized ATS score, measures job-description matching, and provides suggestions to improve the resume.

---

## 🚀 Features

- 📄 Upload resume in PDF format
- 🔍 Extract text from PDF resumes
- 🛠️ Detect predefined technical skills
- 💼 Check GitHub and LinkedIn profiles
- 🎓 Check education and project sections
- 💻 Check experience/internship information
- 📊 Calculate customized ATS score
- 🎯 Compare resume with job description
- 📈 Display skill frequency chart
- 💡 Provide resume improvement suggestions
- 📥 Download ATS analysis report
- 🖥️ Simple and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web application interface |
| **PyPDF2** | PDF text extraction |
| **Pandas** | Data processing and skill-frequency analysis |
| **HTML/CSS** | Interface styling |

---

## ⚙️ How It Works

The application follows the following workflow:

```text
Upload Resume
      ↓
Extract PDF Text
      ↓
Analyze Resume
      ↓
Detect Skills & Profile Information
      ↓
Compare With Job Description
      ↓
Calculate ATS Score
      ↓
Generate Suggestions
      ↓
Display Results & Report
```

---

## 📁 Project Structure

```text
ATS-Resume-Analyzer/
│
├── main.py          # Streamlit application
├── analyzer.py      # Resume analysis and scoring
├── report.py        # Report generation
├── styles.py        # Custom styling
└── README.md        # Project documentation
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Navigate to the Project Folder

```bash
cd ATS-Resume-Analyzer
```

### 3. Install Required Libraries

```bash
pip install streamlit PyPDF2 pandas
```

### 4. Run the Application

```bash
streamlit run main.py
```

### 5. Open the Application

After running the command, Streamlit will provide a local URL.

Open the provided URL in your web browser to use the ATS Resume Analyzer.

---

## 🔮 Future Scope

The project can be further improved by adding:

- 🧠 Natural Language Processing (NLP)
- 🤖 Machine Learning-based resume scoring
- 🔎 Semantic job-description matching
- 📷 OCR support for scanned resumes
- 📚 Larger skill database
- 💼 Improved job recommendations
- 📊 More advanced resume analysis

---

## ⚠️ Current Limitation

The current implementation primarily uses **rule-based and keyword-based analysis**.

Therefore, it does not fully understand the context or semantic meaning of resume content. Future versions can incorporate NLP and machine learning techniques to provide more advanced and context-aware analysis.

---

## 👨‍💻 Author

**Rohin Kumar**

BTech Information Technology Student

Interested in **AI/ML, Data Science, and Python**.

---

## 📌 Project Status

**Completed – Academic / Portfolio Project**
