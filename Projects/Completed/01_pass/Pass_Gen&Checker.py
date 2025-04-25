import random
import re

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    """Generates a random password based on user-specified criteria."""
    
    chars = ""
    if use_uppercase:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lowercase:
        chars += "abcdefghijklmnopqrstuvwxyz"
    if use_numbers:
        chars += "0123456789"
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>/?`"
    
    password = "".join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    """Checks the strength of a password."""
    
    length = len(password) >= 12
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+-=[]{}|;:,.<>/?`]', password))

    score = sum([length, has_uppercase, has_lowercase, has_number, has_special])
    feedback = []
    
    if not length:
        feedback.append("Password should be at least 12 characters long.")
    if not has_uppercase:
        feedback.append("Add at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Add at least one lowercase letter.")
    if not has_number:
        feedback.append("Include at least one number.")
    if not has_special:
        feedback.append("Use at least one special character.")
    
    return score, feedback

def main():
    """Main function to interact with the user and execute password generation and checking."""

    print("Password Generator and Checker")
    
    length = int(input("Enter desired password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
    print("Generated Password:", password)

    score, feedback = check_password_strength(password)
    print("Password Strength Score:", score)
    if feedback:
        print("Password Strength Feedback:")
        for message in feedback:
            print("- " + message)

if __name__ == "__main__":
    main()