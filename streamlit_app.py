# Simple Quiz Game in Python

print("=================================")
print("      Welcome to Quiz Game")
print("=================================")

score = 0

# Questions
questions = [
    {
        "question": "1. What does CPU stand for?",
        "options": ["A. Central Process Unit",
                    "B. Central Processing Unit",
                    "C. Computer Personal Unit",
                    "D. Central Processor Utility"],
        "answer": "B"
    },
    {
        "question": "2. Which programming language is known for AI and Machine Learning?",
        "options": ["A. Python",
                    "B. HTML",
                    "C. CSS",
                    "D. SQL"],
        "answer": "A"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //",
                    "B. <!-- -->",
                    "C. #",
                    "D. **"],
        "answer": "C"
    },
    {
        "question": "4. What is the capital of India?",
        "options": ["A. Mumbai",
                    "B. Chennai",
                    "C. New Delhi",
                    "D. Kolkata"],
        "answer": "C"
    },
    {
        "question": "5. Which function is used to display output in Python?",
        "options": ["A. echo()",
                    "B. print()",
                    "C. output()",
                    "D. display()"],
        "answer": "B"
    }
]

# Quiz Loop
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {q['answer']}.")

# Result
print("\n=================================")
print("           Quiz Result")
print("=================================")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage == 100:
    print("🏆 Excellent! Perfect Score!")
elif percentage >= 80:
    print("🎉 Great Job!")
elif percentage >= 50:
    print("👍 Good! Keep Practicing.")
else:
    print("📚 Better Luck Next Time!")
