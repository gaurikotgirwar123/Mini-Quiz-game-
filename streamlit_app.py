import streamlit as st

# ==============================
# QUIZ GAME
# ==============================

st.set_page_config(page_title="Quiz Game", page_icon="🎯")

st.title("🎯 Quiz Game")
st.write("Test your Python and computer science knowledge")

st.markdown("---")

st.subheader("Minor Project")
st.write("**College:** G.H Raisoni University, Amravati")
st.write("**Course:** Minor Project")

st.write("**Group Members:**")
st.write("• Uday Uttam Kasdekar")
st.write("• Gauri Sunil Kotgirwar")
st.write("• Madhura Dilip Doifode")
st.write("• Niraj Manoj Shirbhate")

st.markdown("---")


# ==============================
# QUIZ QUESTIONS
# ==============================

questions = [
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Computer Processing Utility"
        ],
        "answer": "Central Processing Unit",
        "explanation": "CPU stands for Central Processing Unit. It is often called the brain of a computer."
    },
    {
        "question": "Which programming language is widely used in Artificial Intelligence and Machine Learning?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "Python",
        "explanation": "Python is widely used in AI and Machine Learning because of its simple syntax and powerful libraries."
    },
    {
        "question": "Which symbol is used to write a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#",
        "explanation": "In Python, the # symbol is used to write a single-line comment."
    },
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi",
        "explanation": "New Delhi is the capital city of India."
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["input()", "display()", "print()", "show()"],
        "answer": "print()",
        "explanation": "The print() function is used to display output on the screen."
    },
    {
        "question": "Which of these is a Boolean value in Python?",
        "options": ["True", "10", "Hello", "3.14"],
        "answer": "True",
        "explanation": "Boolean values in Python are True and False."
    },
    {
        "question": "Which operator is used for multiplication in Python?",
        "options": ["+", "*", "x", "%"],
        "answer": "*",
        "explanation": "The * operator is used for multiplication in Python."
    },
    {
        "question": "What does RAM stand for?",
        "options": [
            "Random Access Memory",
            "Read Access Memory",
            "Rapid Access Machine",
            "Random Application Memory"
        ],
        "answer": "Random Access Memory",
        "explanation": "RAM stands for Random Access Memory. It temporarily stores data being used by the computer."
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "def",
        "explanation": "The def keyword is used to define a function in Python."
    },
    {
        "question": "Which language is mainly used to structure web pages?",
        "options": ["Python", "HTML", "C++", "SQL"],
        "answer": "HTML",
        "explanation": "HTML is used to structure the content of web pages."
    },
    {
        "question": "Which operator is used for assignment in Python?",
        "options": ["==", "=", "!=", ">="],
        "answer": "=",
        "explanation": "The = operator assigns a value to a variable."
    },
    {
        "question": "Which Python collection is ordered and changeable?",
        "options": ["Tuple", "List", "Set", "Dictionary"],
        "answer": "List",
        "explanation": "A list is an ordered and changeable collection in Python."
    },
    {
        "question": "Which loop is commonly used to iterate over a sequence?",
        "options": ["for", "if", "def", "try"],
        "answer": "for",
        "explanation": "A for loop is commonly used to iterate through items in a sequence."
    },
    {
        "question": "Which keyword is used for a condition in Python?",
        "options": ["when", "if", "check", "condition"],
        "answer": "if",
        "explanation": "The if keyword is used to execute code based on a condition."
    },
    {
        "question": "What type of memory is RAM?",
        "options": [
            "Permanent memory",
            "Temporary working memory",
            "External memory",
            "Optical memory"
        ],
        "answer": "Temporary working memory",
        "explanation": "RAM temporarily stores data and instructions while programs are running."
    },
    {
        "question": "Which device is commonly used to enter text into a computer?",
        "options": ["Monitor", "Keyboard", "Speaker", "Printer"],
        "answer": "Keyboard",
        "explanation": "A keyboard is an input device used to enter text and commands."
    },
    {
        "question": "Which device displays visual output?",
        "options": ["Keyboard", "Mouse", "Monitor", "Microphone"],
        "answer": "Monitor",
        "explanation": "A monitor is an output device that displays images, text and videos."
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language"
        ],
        "answer": "Hyper Text Markup Language",
        "explanation": "HTML stands for Hyper Text Markup Language."
    },
    {
        "question": "What does CSS mainly control on a web page?",
        "options": ["Database", "Appearance and style", "Python code", "Computer hardware"],
        "answer": "Appearance and style",
        "explanation": "CSS controls the appearance, layout and styling of web pages."
    },
    {
        "question": "Which operator checks whether two values are equal in Python?",
        "options": ["=", "==", "!=", "=>"],
        "answer": "==",
        "explanation": "The == operator compares two values to check whether they are equal."
    },
    {
        "question": "What is a variable?",
        "options": [
            "A storage location for data",
            "A computer screen",
            "A programming language",
            "An operating system"
        ],
        "answer": "A storage location for data",
        "explanation": "A variable is a name used to store a value in a program."
    },
    {
        "question": "Which of these is an integer?",
        "options": ["10", "10.5", '"10"', "True"],
        "answer": "10",
        "explanation": "An integer is a whole number without a decimal point."
    },
    {
        "question": "Which of these is a string in Python?",
        "options": ["25", "3.14", '"Hello"', "True"],
        "answer": '"Hello"',
        "explanation": "A string is a sequence of characters enclosed in quotes."
    },
    {
        "question": "Which language is commonly used to manage data in relational databases?",
        "options": ["HTML", "SQL", "CSS", "Python"],
        "answer": "SQL",
        "explanation": "SQL is commonly used to store, retrieve and manage data in relational databases."
    },
    {
        "question": "What is an algorithm?",
        "options": [
            "A step-by-step procedure to solve a problem",
            "A computer screen",
            "A type of hardware",
            "A programming error"
        ],
        "answer": "A step-by-step procedure to solve a problem",
        "explanation": "An algorithm is a step-by-step procedure used to solve a problem."
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue",
        "explanation": "FIFO means First In, First Out. A queue follows this principle."
    },
    {
        "question": "Which data structure follows LIFO?",
        "options": ["Queue", "Stack", "Array", "Graph"],
        "answer": "Stack",
        "explanation": "LIFO means Last In, First Out. A stack follows this principle."
    },
    {
        "question": "What is debugging?",
        "options": [
            "Finding and fixing errors in a program",
            "Writing a new computer",
            "Deleting an operating system",
            "Creating hardware"
        ],
        "answer": "Finding and fixing errors in a program",
        "explanation": "Debugging is the process of finding and fixing errors or bugs in a program."
    },
    {
        "question": "Which of these is an operating system?",
        "options": ["Windows", "Python", "HTML", "Google"],
        "answer": "Windows",
        "explanation": "Windows is an operating system developed by Microsoft."
    },
    {
        "question": "What does AI stand for?",
        "options": [
            "Artificial Intelligence",
            "Automated Internet",
            "Advanced Information",
            "Artificial Internet"
        ],
        "answer": "Artificial Intelligence",
        "explanation": "AI stands for Artificial Intelligence, which enables computers to perform tasks that normally require human intelligence."
    }
]


# ==============================
# SESSION STATE
# ==============================

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None


# ==============================
# QUIZ
# ==============================

if st.session_state.current_question < len(questions):

    q = questions[st.session_state.current_question]

    st.subheader(
        f"Question {st.session_state.current_question + 1} of {len(questions)}"
    )

    st.write(f"### {q['question']}")

    if not st.session_state.answered:

        selected = st.radio(
            "Choose your answer:",
            q["options"],
            index=None,
            key=f"question_{st.session_state.current_question}"
        )

        if st.button("Submit Answer"):

            if selected is None:
                st.warning("⚠️ Please select an answer first.")
            else:
                st.session_state.selected_answer = selected
                st.session_state.answered = True

                if selected == q["answer"]:
                    st.session_state.score += 1

                st.rerun()

    else:

        if st.session_state.selected_answer == q["answer"]:

            st.success("✅ Correct!")

        else:

            st.error("❌ Wrong!")

            st.write(
                f"**Correct answer:** {q['answer']}"
            )

        st.info(f"💡 **Explanation:** {q['explanation']}")

        if st.button("➡️ Next Question"):

            st.session_state.current_question += 1
            st.session_state.answered = False
            st.session_state.selected_answer = None

            st.rerun()


# ==============================
# FINAL RESULT
# ==============================

else:

    st.success("🎉 Quiz Completed!")

    score = st.session_state.score
    total = len(questions)
    percentage = (score / total) * 100

    st.write(f"## Your Score: {score} / {total}")
    st.write(f"### Percentage: {percentage:.1f}%")

    if percentage >= 80:
        st.success("🏆 Excellent! Great knowledge!")
    elif percentage >= 50:
        st.info("👍 Good job! Keep learning!")
    else:
        st.warning("📚 Keep practicing. You can do even better!")

    if st.button("🔄 Start Again"):

        st.session_state.clear()
        st.rerun()
