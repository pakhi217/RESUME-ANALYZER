# 🚀 AI Resume & Skill Gap Analyzer

> Turn your resume into a **clear roadmap for success**

---

## 📌 Overview

The **AI Resume & Skill Gap Analyzer** helps students and job seekers understand where they stand and what they need to improve.

Upload your resume, select your target role, and get:

* 📊 A **match score**
* ❌ Missing skills
* ✅ Personalized improvement suggestions
* 🛤️ A structured learning roadmap

---

## 🎯 Problem Statement

Most students don’t know:

* What skills they are missing
* How far they are from their target job
* What to do next

As a result, they waste time learning random things without direction.

---

## 💡 Our Solution

This project provides a **role-based resume analysis system** that:

* Compares your resume with industry requirements
* Identifies skill gaps
* Suggests **specific actions**, not generic advice

---

## ⚙️ Features

### 🔍 Resume Parsing

* Upload PDF resumes
* Extracts and processes text automatically

### 🎯 Role-Based Analysis

* Choose target roles like:

  * Software Engineer
  * Data Scientist
  * ECE Engineer

### 📊 Match Score

* Calculates how well your resume fits the selected role

### 🧠 Skill Gap Detection

* Highlights missing skills clearly

### 🛠️ Actionable Suggestions

* Recommends projects and tools to learn
* Provides practical next steps

### 🛤️ Learning Roadmap

* Structured plan (30–60 days) to improve your profile

---

## 🏗️ Tech Stack

**Frontend:**

* HTML, CSS, JavaScript *(or React)*

**Backend:**

* Python (Flask / FastAPI)

**Libraries & Tools:**

* pdfplumber / PyPDF2 (resume parsing)
* OpenAI API *(optional for suggestions)*

---

## 🧠 How It Works

1. Upload your resume (PDF)
2. Select your target role
3. System extracts skills from your resume
4. Compares with predefined role requirements
5. Generates:

   * Match Score
   * Missing Skills
   * Suggestions
   * Roadmap

---

## 📂 Project Structure

```
resume-analyzer/
│
├── backend/
│   ├── app.py
│   ├── parser.py
│   ├── analyzer.py
│   └── roles_data.json
│
├── frontend/
│   ├── index.html
│   ├── dashboard.html
│   ├── style.css
│   └── script.js
│
└── uploads/
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the backend

```bash
python app.py
```

### 4. Open frontend

Open `index.html` in your browser

---

## 📊 Example Output

* Match Score: **65%**
* Missing Skills: Machine Learning, Data Structures
* Suggestions:

  * Build a spam classifier
  * Practice DSA problems
* Roadmap:

  * Week 1–2: Learn basics
  * Week 3–4: Build project

---

## 🌟 Future Improvements

* Real-time job matching
* Advanced NLP for better skill extraction
* Resume scoring based on ATS systems
* Multi-language support

---

## 🤝 Contributors

* Pakhi Saxena
* Ishita Singh

---

## 📜 License

This project is open-source and available under the MIT License

---

## 💬 Final Note

This project is built to **guide students with clarity**, not just analyze resumes.
The goal is simple:

> Replace confusion with direction.
