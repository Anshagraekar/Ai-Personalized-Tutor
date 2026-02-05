import streamlit as st
import pandas as pd

# ==========================
# LOAD DATA
# ==========================
quiz_df = pd.read_excel("history_quiz_by_grade_and_domain.xlsx")
videos_df = pd.read_excel("videos.xlsx")

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="AI Tutor – Personalized Learning",
    layout="wide"
)

st.title("🎓 AI Tutor – Quiz Based Recommendation System")

# ==========================
# SIDEBAR INPUTS
# ==========================
st.sidebar.header("Student Input")

grade = st.sidebar.selectbox(
    "Select Grade",
    sorted(quiz_df["grade"].unique())
)

domains = quiz_df[quiz_df["grade"] == grade]["domain"].unique()
domain = st.sidebar.selectbox("Select Domain", domains)

# ==========================
# LOAD QUIZ
# ==========================
quiz = quiz_df[
    (quiz_df["grade"] == grade) &
    (quiz_df["domain"] == domain)
].reset_index(drop=True)

st.subheader(f"📘 Quiz: {domain}")

# ==========================
# QUIZ UI
# ==========================
user_answers = []
correct = 0
total = len(quiz)

for i, row in quiz.iterrows():
    st.markdown(f"**Q{i+1}. {row['question']}**")

    # 🔹 FIX: Proper option labels
    options = {
        "A": row["option_a"],
        "B": row["option_b"],
        "C": row["option_c"],
        "D": row["option_d"]
    }

    selected = st.radio(
        label="",
        options=list(options.keys()),
        format_func=lambda x: f"{x}) {options[x]}",
        key=f"q_{i}"
    )

    user_answers.append(selected)

    if selected == row["correct_option"]:
        correct += 1

# ==========================
# SUBMIT BUTTON
# ==========================
if st.button("Submit Quiz"):
    if total == 0:
        st.error("❌ No questions found for this domain.")
    else:
        score = (correct / total) * 100

        # --------------------------
        # STUDENT CLASSIFICATION
        # --------------------------
        if score < 40:
            student_type = "Weak"
            difficulty = "easy"
        elif score < 70:
            student_type = "Average"
            difficulty = "medium"
        else:
            student_type = "Strong"
            difficulty = "hard"

        # --------------------------
        # DISPLAY RESULT
        # --------------------------
        st.success(f"📊 Score: {score:.2f}%")
        st.info(f"📌 Student Type: {student_type}")

        # --------------------------
        # VIDEO RECOMMENDATION
        # --------------------------
        st.subheader("📺 Recommended Videos")

        recommended_videos = videos_df[
            (videos_df["grade"] == grade) &
            (videos_df["domain"] == domain) &
            (videos_df["difficulty"].str.lower() == difficulty)
        ]

        # 🔒 SCHEMA-SAFE VIDEO LINK HANDLING (NO KeyError EVER)
        possible_link_cols = [
            "video_url",
            "url",
            "video_link",
            "link",
            "youtube_link",
            "videoid",
            "video_id"
        ]

        video_link_col = next(
            (col for col in possible_link_cols if col in videos_df.columns),
            None
        )

        if video_link_col is None:
            st.error("❌ No video link column found in videos.xlsx")
            st.write("Available columns:", list(videos_df.columns))
        elif recommended_videos.empty:
            st.warning("⚠️ No videos available for this level.")
        else:
            for _, v in recommended_videos.iterrows():
                st.markdown(
                    f"- **{v['concept']}** ({v['difficulty']})  \n"
                    f"  🔗 {v[video_link_col]}"
                )
