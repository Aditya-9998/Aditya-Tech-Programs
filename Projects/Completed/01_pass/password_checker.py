import re
import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password_strength(password):
    length = len(password) >= 12
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = sum([length, has_upper, has_lower, has_number, has_special])
    feedback = []

    if not length:
        feedback.append("Password should be at least 12 characters long for having a strong password.")
    if not has_upper:
        feedback.append("Add at least one uppercase letter.")
    if not has_lower:
        feedback.append("Add at least one lowercase letter.")
    if not has_number:
        feedback.append("Include at least one number.")
    if not has_special:
        feedback.append("Use at least one special character.")

    if score == 5 and length:
        feedback = ["You remain carefree. The password you provided is very strong."]

    return score, feedback

# Function to generate random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# GUI Functions
def check_password():
    password = password_entry.get()
    score, feedback = check_password_strength(password)

    strength_labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_label.config(text=f"Strength: {strength_labels[score-1] if score else 'Very Weak'}")

    feedback_text.delete(1.0, tk.END)
    for tip in feedback:
        feedback_text.insert(tk.END, f"- {tip}\n")

def generate_random_password():
    length = int(length_entry.get())
    random_password = generate_password(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)
    messagebox.showinfo("Password Generated", "A new password has been generated and filled in the input box.")

# Main Application Window
root = tk.Tk()
root.title("Password Checker and Generator")
root.geometry("500x400")

# Widgets
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password)
check_button.pack(pady=5)

strength_label = tk.Label(root, text="Strength:", font=("Arial", 12, "bold"))
strength_label.pack(pady=10)

feedback_label = tk.Label(root, text="Feedback:")
feedback_label.pack(pady=5)

feedback_text = tk.Text(root, width=50, height=10, wrap="word")
feedback_text.pack(pady=5)

length_label = tk.Label(root, text="Password Length for Generator:")
length_label.pack(pady=5)

length_entry = tk.Entry(root, width=10)
length_entry.insert(0, "12")  # Default value
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_random_password)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
