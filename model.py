import pandas as pd

# ==========================
# LOAD DATA
# ==========================

quiz_df = pd.read_excel("history_quiz_by_grade_and_domain.xlsx")
videos_df = pd.read_excel("videos.xlsx")


# ==========================
# STEP 1: SHOW DOMAINS
# ==========================

def show_domains(grade):
    domains = quiz_df[quiz_df["grade"] == grade]["domain"].unique()
    print("\n📚 Available Domains:")
    for i, d in enumerate(domains, 1):
        print(f"{i}. {d}")
    return domains


# ==========================
# STEP 2: LOAD QUIZ
# ==========================

def load_quiz(grade, domain):
    return quiz_df[
        (quiz_df["grade"] == grade) &
        (quiz_df["domain"] == domain)
    ]


# ==========================
# STEP 3: CONDUCT QUIZ
# ==========================

def conduct_quiz(quiz):
    print("\n📝 Starting Quiz...\n")
    answers = {}

    for idx, row in quiz.iterrows():
        print(f"Q{idx+1}. {row['question']}")
        print(f"A) {row['option_a']}")
        print(f"B) {row['option_b']}")
        print(f"C) {row['option_c']}")
        print(f"D) {row['option_d']}")
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        answers[row["question_id"]] = ans
        print("-" * 40)

    return answers


# ==========================
# STEP 4: EVALUATE QUIZ
# ==========================

def evaluate_quiz(quiz, answers):
    correct = 0

    for _, row in quiz.iterrows():
        if answers.get(row["question_id"]) == row["correct_option"]:
            correct += 1

    total = len(quiz)
    score = (correct / total) * 100
    return score


# ==========================
# STEP 5: CLASSIFY STUDENT
# ==========================

def classify_student(score):
    if score < 40:
        return "Weak", "easy"
    elif score < 70:
        return "Average", "medium"
    else:
        return "Strong", "hard"


# ==========================
# STEP 6: RECOMMEND VIDEOS
# ==========================

def recommend_videos(grade, domain, difficulty):
    return videos_df[
        (videos_df["grade"] == grade) &
        (videos_df["domain"] == domain) &
        (videos_df["difficulty"].str.lower() == difficulty)
    ]


# ==========================
# MAIN PROGRAM
# ==========================

def main():
    print("\n🎓 AI Tutor – Quiz-Based Recommendation System\n")

    grade = int(input("Enter Class (6–12): "))
    domains = show_domains(grade)

    choice = int(input("\nSelect domain number: "))
    domain = domains[choice - 1]

    quiz = load_quiz(grade, domain)
    answers = conduct_quiz(quiz)

    score = evaluate_quiz(quiz, answers)
    student_type, difficulty = classify_student(score)

    print(f"\n📊 Your Score: {score:.2f}%")
    print(f"📌 Student Type: {student_type}")

    videos = recommend_videos(grade, domain, difficulty)

    print("\n📺 Recommended Videos:")
    for _, row in videos.iterrows():
        print(f"""
▶ Concept  : {row['concept']}
▶ Difficulty : {row['difficulty']}
▶ Video ID : {row['video_id']}
▶ URL      : {row['url']}
""")

# ==========================
# RUN
# ==========================

if __name__ == "__main__":
    main()