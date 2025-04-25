from fpdf import FPDF

# Create PDF class instance
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Project Report: Password Strength Checker and Generator', align='C', ln=1)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

# Initialize PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font('Arial', '', 12)

# Add content to PDF
content = """
1. Project Overview
This project is a Python-based program designed to assess the strength of user-created passwords and generate strong, secure passwords. 
It has two primary functionalities:
- Password Strength Checker: Evaluates a password based on specific security criteria and provides feedback.
- Password Generator: Creates random, strong passwords meeting standard security guidelines.

2. Objectives
- Enhance password security by educating users about strong passwords.
- Provide tools to help users create robust passwords that are resistant to brute force attacks or common exploits.

3. Features
1. Password Strength Evaluation:
   - Checks the following criteria:
     - Minimum length (12 characters).
     - Presence of uppercase and lowercase letters.
     - Inclusion of numeric digits.
     - Use of special characters.
   - Assigns a strength score (Very Weak to Very Strong).
   - Provides feedback for improving weak passwords.
2. Password Generator:
   - Creates a password of a specified length.
   - Includes a mix of uppercase, lowercase, digits, and special characters.
3. User-Friendly Interface:
   - Simple input prompts and detailed feedback messages.

4. Technologies Used
1. Python Programming Language:
   - Core language for implementation.
2. Modules:
   - re: For pattern matching to validate password structure.
   - random and string: To generate secure random passwords.
3. Logic and Algorithms:
   - Use of regular expressions to efficiently validate password content.
   - Iterative feedback mechanism to guide users toward stronger passwords.

5. Code Functionality
1. Password Strength Checker:
   - Validates user input based on predefined rules.
   - Uses a scoring system to classify password strength.
   - Provides actionable feedback.
2. Password Generator:
   - Randomly selects characters from a pool of letters, numbers, and symbols.
   - Ensures the generated password meets strong security standards.
3. Main Program:
   - Accepts user input and interacts with the checker and generator functions.
   - Displays password strength and improvement tips.

6. Project Workflow
1. User Input:
   - User enters a password for evaluation.
   - Alternatively, the user can request a randomly generated password.
2. Password Validation:
   - The system evaluates the password and returns:
     - A score (Very Weak to Very Strong).
     - Feedback on areas needing improvement.
3. Output:
   - For weak passwords: Suggestions to improve.
   - For strong passwords: A confirmation message.
4. Optional Password Generation:
   - Users can request a generated password to meet strength criteria.

7. Benefits
- Educational Value:
   - Educates users about password best practices.
- Enhanced Security:
   - Ensures users adopt strong password practices.
- Ease of Use:
   - Simple interface with actionable suggestions.

8. Potential Enhancements
1. Graphical User Interface (GUI):
   - Build a user-friendly interface for non-technical users.
2. Integration with Applications:
   - Embed the tool into websites or software requiring password creation.
3. Customizable Feedback:
   - Tailor suggestions based on specific use cases (e.g., corporate policies).
4. Multi-language Support:
   - Provide feedback in different languages.

9. Conclusion
The Password Strength Checker and Generator is a practical tool for improving password security. By educating users and offering secure password generation, this project contributes to reducing vulnerabilities associated with weak passwords. It is an excellent foundation for further development and integration into broader security applications.
"""

pdf.multi_cell(0, 10, content)

# Save as PDF
file_path = "Password_Strength_Project_Report.pdf"
pdf.output(file_path)
file_path
file_path = "C:/Users/Aditya Kumar/Documents/Password_Strength_Project_Report.pdf"
pdf.output(file_path)