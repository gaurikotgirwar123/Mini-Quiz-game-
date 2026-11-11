import streamlit as st

# -----------------------------
# QUIZ QUESTIONS
# -----------------------------

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
        "options": [
            "Python",
            "HTML",
            "CSS",
            "SQL"
        ],
        "answer": "Python",
        "explanation": "Python is widely used in AI and Machine Learning because of its simple syntax and powerful libraries."
    },
    {
        "question": "Which symbol is used to write a single-line comment in Python?",
        "options": [
            "#",
            "//",
            "/*",
            "<!--"
        ],
        "answer": "#",
        "explanation": "In Python, the # symbol is used to create a single-line comment."
    },
    {
        "question": "What is the capital of India?",
        "options": [
            "Mumbai",
            "New Delhi",
            "Kolkata",
            "Chennai"
        ],
        "answer": "New Delhi",
        "explanation": "New Delhi is the capital city of India."
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": [
            "input()",
            "display()",
            "print()",
            "show()"
        ],
        "answer": "print()",
        "explanation": "The print() function is used to display text or other values on the screen."
    },
    {
        "question": "Which data type stores True or False values in Python?",
        "options": [
            "String",
            "Boolean",
            "Integer",
            "Float"
        ],
        "answer": "Boolean",
        "explanation": "The Boolean data type stores one of two values: True or False."
    },
    {
        "question": "Which operator is used for multiplication in Python?",
        "options": [
            "+",
            "-",
            "*",
            "/"
        ],
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
        "options": [
            "function",
            "define",
            "def",
            "fun"
        ],
        "answer": "def",
        "explanation": "The def keyword is used to define a function in Python."
    },
    {
        "question": "Which language is mainly used to create the structure of web pages?",
        "options": [
            "Python",
            "HTML",
            "C++",
            "SQL"
        ],
        "answer": "HTML",
        "explanation": "HTML is used to create the basic structure and content of web pages."
    },
    {
        "question": "Which operator is used for assignment in Python?",
        "options": [
            "==",
            "=",
            "!=",
            ">="
        ],
        "answer": "=",
        "explanation": "The = operator assigns a value to a variable."
    },
    {
        "question": "Which Python collection is ordered and changeable?",
        "options": [
            "Tuple",
            "List",
            "Set",
            "String"
        ],
        "answer": "List",
        "explanation": "A Python list is ordered and mutable, meaning its elements can be changed."
    },
    {
        "question": "Which loop is commonly used to repeat over a sequence in Python?",
        "options": [
            "for loop",
            "switch loop",
            "repeat loop",
            "select loop"
        ],
        "answer": "for loop",
        "explanation": "A for loop is commonly used to iterate through items in a sequence."
    },
    {
        "question": "Which keyword is used to make a decision in Python?",
        "options": [
            "if",
            "when",
            "check",
            "case"
        ],
        "answer": "if",
        "explanation": "The if keyword is used to execute code when a condition is true."
    },
    {
        "question": "Which type of memory is used as temporary working memory by a computer?",
        "options": [
            "ROM",
            "RAM",
            "Hard Disk",
            "SSD"
        ],
        "answer": "RAM",
        "explanation": "RAM provides temporary working memory for programs and data currently in use."
    },
    {
        "question": "Which device is commonly used to enter text into a computer?",
        "options": [
            "Monitor",
            "Printer",
            "Keyboard",
            "Speaker"
        ],
        "answer": "Keyboard",
        "explanation": "A keyboard is an input device commonly used to enter text and commands."
    },
    {
        "question": "Which device displays visual output from a computer?",
        "options": [
            "Keyboard",
            "Monitor",
            "Mouse",
            "Microphone"
        ],
        "answer": "Monitor",
        "explanation": "A monitor is an output device that displays visual information."
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyperlink Text Management Language",
            "Home Tool Markup Language"
        ],
        "answer": "Hyper Text Markup Language",
        "explanation": "HTML stands for Hyper Text Markup Language."
    },
    {
        "question": "What is CSS mainly used for?",
        "options": [
            "Database management",
            "Styling web pages",
            "Writing Python programs",
            "Managing computer memory"
        ],
        "answer": "Styling web pages",
        "explanation": "CSS is used to control the appearance and layout of web pages."
    },
    {
        "question": "Which operator checks whether two values are equal in Python?",
        "options": [
            "=",
            "==",
            "!=",
            "=>"
        ],
        "answer": "==",
        "explanation": "The == operator compares two values and checks whether they are equal."
    },
    {
        "question": "What is a variable in programming?",
        "options": [
            "A storage name for a value",
            "A type of computer",
            "A programming language",
            "A hardware device"
        ],
        "answer": "A storage name for a value",
        "explanation": "A variable is a named reference used to store or represent a value."
    },
    {
        "question": "Which of these is an integer?",
        "options": [
            "10",
            "10.5",
            "\"10\"",
            "True"
        ],
        "answer": "10",
        "explanation": "10 is an integer because it is a whole number without a decimal point."
    },
    {
        "question": "Which of these is a string in Python?",
        "options": [
            "25",
            "3.14",
            "\"Hello\"",
            "False"
        ],
        "answer": "\"Hello\"",
        "explanation": "A string is a sequence of characters enclosed in quotes."
    },
    {
        "question": "Which language is commonly used to communicate with databases?",
        "options": [
            "SQL",
            "HTML",
            "CSS",
            "XML"
        ],
        "answer": "SQL",
        "explanation": "SQL stands for Structured Query Language and is commonly used to work with databases."
    },
    {
        "question": "What is an algorithm?",
        "options": [
            "A step-by-step procedure for solving a problem",
            "A computer screen",
            "A programming language",
            "A type of hardware"
        ],
        "answer": "A step-by-step procedure for solving a problem",
        "explanation": "An algorithm is a sequence of well-defined steps used to solve a problem."
    },
    {
        "question": "Which data structure follows FIFO (First In, First Out)?",
        "options": [
            "Stack",
            "Queue",
            "Tree",
            "Graph"
        ],
        "answer": "Queue",
        "explanation": "A queue follows FIFO, meaning the first element added is the first one removed."
    },
    {
        "question": "Which data structure follows LIFO (Last In, First Out)?",
        "options": [
            "Queue",
            "Stack",
            "Array",
            "Graph"
        ],
        "answer": "Stack",
        "explanation": "A stack follows LIFO, meaning the last element added is the first one removed."
    },
    {
        "question": "What is debugging?",
        "options": [
            "Finding and fixing errors in a program",
            "Creating a computer",
            "Installing an operating system",
            "Designing a website"
        ],
        "answer": "Finding and fixing errors in a program",
        "explanation": "Debugging is the process of finding and correcting errors or bugs in a program."
    },
    {
        "question": "Which of the following is an operating system?",
        "options": [
            "Python",
            "Windows",
            "HTML",
            "Google"
        ],
        "answer": "Windows",
        "explanation": "Windows is an operating system that manages computer hardware and software resources."
    },
    {
        "question": "What does AI stand for?",
        "options": [
            "Automated Internet",
            "Artificial Intelligence",
            "Advanced Information",
            "Artificial Internet"
        ],
        "answer": "Artificial Intelligence",
        "explanation": "AI stands for Artificial Intelligence, which involves creating systems capable of performing tasks that normally require human intelligence."
    }
]


# -----------------------------
# SESSION STATE
# -----------------------------

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None


# -----------------------------
# TITLE
# -----------------------------

st.title("Quiz Game")
st.write("Test your Python and computer science knowledge")

st.divider()


# -----------------------------
# QUIZ
# -----------------------------

if st.session_state.current_question < len(questions):

    q = questions[st.session_state.current_question]

    st.subheader(
        f"Question {st.session_state.current_question + 1} of {len(questions)}"
    )

    st.write(f"### {q['question']}")

    # Before answering
    if not st.session_state.answered:

        selected = st.radio(
            "Choose your answer:",
            q["options"],
            index=None,
            key=f"question_{st.session_state.current_question}"
        )

        if st.button("Submit Answer", type="primary"):

            if selected is None:
                st.warning("⚠️ Please select an answer first.")

            else:
                st.session_state.selected_answer = selected
                st.session_state.answered = True

                if selected == q["answer"]:
                    st.session_state.score += 1

                st.rerun()

    # After answering
    else:

        selected = st.session_state.selected_answer

        if selected == q["answer"]:

            st.success("✅ Correct!")

        else:

            st.error("❌ Wrong!")

            st.write(f"**Correct answer:** {q['answer']}")

        st.info(f"💡 **Explanation:** {q['explanation']}")

        st.divider()

        if st.session_state.current_question < len(questions) - 1:

            if st.button("Next Question ➡️", type="primary"):

                st.session_state.current_question += 1
                st.session_state.answered = False
                st.session_state.selected_answer = None

                st.rerun()

        else:

            if st.button("See Final Score 🏆", type="primary"):

                st.session_state.current_question += 1

                st.rerun()


# -----------------------------
# FINAL SCORE
# -----------------------------

else:

    score = st.session_state.score
    total = len(questions)
    percentage = (score / total) * 100

    st.title("🎉 Quiz Completed!")

    st.write(f"## Your Score: {score}/{total}")

    st.write(f"### Percentage: {percentage:.1f}%")

    if percentage == 100:
        st.success("🏆 Perfect score! Amazing!")

    elif percentage >= 80:
        st.success("🌟 Excellent work!")

    elif percentage >= 60:
        st.info("👍 Good job! Keep practicing.")

    elif percentage >= 40:
        st.warning("📚 Not bad! A little more practice will help.")

    else:
        st.error("💪 Keep learning and try again!")

    st.divider()

    if st.button("🔄 Start Again", type="primary"):

        st.session_state.clear()

        st.rerun()
