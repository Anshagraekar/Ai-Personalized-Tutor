# Ai-Personalized-Tutor
An intelligent education system that analyzes student performance, identifies weak concepts, and recommends personalized videos, practice tests, and revision plans using rule-based logic + machine learning (Random Forest).
An intelligent education system that analyzes student performance, identifies weak concepts, and recommends personalized videos, practice tests, and revision plans using rule-based logic + machine learning (Random Forest).
.

📌 Project Overview

The AI Tutor – Personalized Learning Recommendation System analyzes a student’s quiz performance to classify their learning level and recommend appropriate learning resources. The system adapts content difficulty based on student proficiency, ensuring a more effective and personalized learning experience.

This project demonstrates the practical application of AI and ML in educational technology.

🚀 Features

📘 Quiz-based student assessment

🧠 Student classification (Weak / Average / Strong)

🤖 Machine Learning support using Random Forest

🎯 Difficulty-based content recommendation

📺 Video recommendations by grade & domain

🖥️ Interactive UI built with Streamlit

📊 Performance evaluation and feedback

🏗️ System Architecture
User Input (Grade & Domain)
        ↓
Quiz Evaluation
        ↓
Performance Analysis
        ↓
Student Classification (Rule-Based / ML)
        ↓
Recommendation Engine
        ↓
Personalized Learning Output

🧪 Machine Learning Model

Algorithm: Random Forest Classifier

Purpose: Classify students based on quiz performance

Input Features:

Quiz score

Accuracy

Correct answers

Output Classes:

Weak

Average

Strong

A rule-based fallback mechanism is used when ML prediction is unavailable.

🖥️ User Interface

Built using Streamlit

Displays:

Quiz questions

Answer options

Student performance results

Recommended learning videos

Streamlit was chosen for its simplicity and seamless integration with Python-based ML workflows.

🛠️ Technologies Used
Category	Tools
Programming	Python
UI Framework	Streamlit
Machine Learning	scikit-learn
Data Processing	pandas, NumPy
Dataset Format	Excel (.xlsx)
📂 Project Structure
ai_tutor/
│
├── app.py
├── history_quiz_by_grade_and_domain.xlsx
├── videos.xlsx
├── student_performance.xlsx
├── README.md

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-tutor.git
cd ai-tutor

2️⃣ Install Dependencies
pip install streamlit pandas openpyxl scikit-learn

3️⃣ Run the Application
python -m streamlit run app.py


The application will open automatically in your browser.

📊 Dataset Description

Quiz Dataset: Contains questions, options, correct answers, grade, and domain

Video Dataset: Contains learning videos mapped by grade, domain, and difficulty

Student Performance Dataset: Used for training the Random Forest classifier

🎯 Use Case

Personalized learning platforms

Adaptive educational systems

AI-based tutoring systems

Final-year AI / ML academic projects

📜 License

This project is intended for educational use only.

🙌 Acknowledgments

NCERT-aligned content for quiz design

Open-source Python libraries

Streamlit community
