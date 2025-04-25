import random

# Questions and Answers
data = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": 1},
    {"question": "What is 5 + 7?", "options": ["10", "12", "14", "15"], "answer": 2},
    {"question": "Who wrote 'Hamlet'?", "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "J.K. Rowling"], "answer": 2},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": 3},
    {"question": "What is the boiling point of water?", "options": ["50°C", "100°C", "150°C", "200°C"], "answer": 2}
]

# Shuffle questions
random.shuffle(data)

def run_quiz():
    score = 0

    print("Welcome to the Quiz Game!\n")

    for i, item in enumerate(data):
        print(f"Question {i + 1}: {item['question']}")

        for idx, option in enumerate(item['options'], 1):
            print(f"  {idx}. {option}")

        while True:
            try:
                user_answer = int(input("Enter your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        if user_answer == item['answer']:
            print("Correct!\n")
            score += 1
        else:
            correct_option = item['options'][item['answer'] - 1]
            print(f"Wrong! The correct answer was: {correct_option}\n")

    print(f"Your final score is: {score}/{len(data)}")
    if score == len(data):
        print("Excellent! You got all answers right!")
    elif score > len(data) / 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    run_quiz()