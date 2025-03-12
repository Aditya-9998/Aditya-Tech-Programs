from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    length = len(password) >= 12
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', password))

    score = sum([length, has_upper, has_lower, has_number, has_special])
    feedback = []

    if not length:
        feedback.append("Password should be at least 12 characters long for having a STRONG password.")
    if not has_upper:
        feedback.append("Add at least one uppercase letter.")
    if not has_lower:
        feedback.append("Add at least one lowercase letter.")
    if not has_number:
        feedback.append("Include at least one number.")
    if not has_special:
        feedback.append("Use at least one special character.")

    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"][score - 1 if score else 0]
    return strength, feedback

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password', '')
    strength, feedback = check_password_strength(password)
    return jsonify({"strength": strength, "feedback": feedback})

if __name__ == '__main__':
    app.run(debug=True)
