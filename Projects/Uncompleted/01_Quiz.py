import tkinter as tk
from tkinter import messagebox
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

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")
        self.current_question = 0
        self.score = 0

        # Question Label
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        # Option Buttons
        self.options = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 14), command=lambda idx=i: self.check_answer(idx + 1))
            button.pack(pady=5)
            self.options.append(button)

        # Next Button
        self.next_button = tk.Button(root, text="Next", font=("Arial", 14), command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=20)

        # Score Label
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        # Load First Question
        self.load_question()

    def load_question(self):
        question_data = data[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {question_data['question']}")
        for idx, option in enumerate(question_data["options"]):
            self.options[idx].config(text=option, state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, selected):
        question_data = data[self.current_question]
        correct = question_data["answer"]
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            correct_option = question_data["options"][correct - 1]
            messagebox.showerror("Wrong!", f"Correct answer: {correct_option}")
        for button in self.options:
            button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.score_label.config(text=f"Score: {self.score}")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(data):
            self.load_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your final score is: {self.score}/{len(data)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
