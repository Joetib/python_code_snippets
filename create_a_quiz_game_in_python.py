# Let's create a simple quiz game in Python
# We will use a list of questions and their corresponding answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Who painted the Mona Lisa?",
    "What is the chemical symbol for gold?",
    "What is the tallest mountain in the world?"
]
answers = ["Paris", "Jupiter", "Leonardo da Vinci", "Au", "Mount Everest"]
score = 0
# Loop through the questions and ask the user for their answer
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Enter your answer: ")
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
# Print the final score
print("Your score is:", score)