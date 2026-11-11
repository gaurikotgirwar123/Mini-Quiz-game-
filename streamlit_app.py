import streamlit as st

st.title("🎯 Welcome to Quiz Game")
st.write("Test your Python and Computer Science knowledge!")

questions = [
    {
        "question": "1. What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Central Processing Unit",
            "C. Computer Personal Unit",
            "D. Central Processor Utility"
        ],
        "answer": "B. Central Processing Unit"
    },
    {
        "question": "2. Which programming language is known for AI and Machine Learning?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A. Python"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C. #"
    },
    {
        "question": "4. What is the capital of India?",
        "options": ["A. Mumbai", "B. Chennai", "C. New Delhi", "D. Kolkata"],
        "answer": "C. New Delhi"
    },
    {
        "question": "5. Which function is used to display output in Python?",
        "options": ["A. echo()", "B. print()", "C. output()", "D. display()"],
        "answer": "B. print()"
    },
    {
        "question": "6. Which data type is used to store True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C. Boolean"
    },
    {
        "question": "7. Which symbol is used for multiplication in Python?",
        "options": ["A. x", "B. *", "C. #", "D. %"],
        "answer": "B. *"
    },
    {
        "question": "8. What is the full form of RAM?",
        "options": [
            "A. Random Access Memory",
            "B. Read Access Memory",
            "C. Rapid Access Machine",
            "D. Random Application Memory"
        ],
        "answer": "A. Random Access Memory"
    },
    {
        "question": "9. Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C. def"
    },
    {
        "question": "10. Which language is mainly used to structure web pages?",
        "options": ["A. Python", "B. HTML", "C. SQL", "D. C++"],
        "answer": "B. HTML"
    }
]

with st.form("quiz_form"):
    answers = []

    for q in questions:
        answer = st.radio(
            q["question"],
            q["options"],
            index=None
        )
        answers.append(answer)

    submitted = st.form_submit_button("Submit Quiz")

if submitted:
    score = 0

    for i in range(len(questions)):
        if answers[i] == questions[i]["answer"]:
            score += 1

    percentage = (score / len(questions)) * 100

    st.subheader("🏆 Quiz Result")
    st.write(f"**Your Score: {score}/10**")
    st.write(f"**Percentage: {percentage:.2f}%**")

    if percentage == 100:
        st.success("🏆 Excellent! Perfect Score!")
    elif percentage >= 80:
        st.success("🎉 Great Job!")
    elif percentage >= 50:
        st.info("👍 Good! Keep Practicing.")
    else:
        st.warning("📚 Better Luck Next Time!")

    if st.button("🔄 Start Again"):
        st.rerun()
