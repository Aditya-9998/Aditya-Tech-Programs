const generateBtn = document.getElementById('generateBtn');
const copyBtn = document.getElementById('copyBtn');
const passwordField = document.getElementById('password');
const lengthInput = document.getElementById('length');
const includeUppercase = document.getElementById('includeUppercase');
const includeLowercase = document.getElementById('includeLowercase');
const includeNumbers = document.getElementById('includeNumbers');
const includeSpecial = document.getElementById('includeSpecial');
const checkBtn = document.getElementById('checkBtn');
const passwordInput = document.getElementById('passwordInput');
const feedbackDiv = document.getElementById('feedback');

const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
const numbers = '0123456789';
const specialChars = '!@#$%^&*()-_=+[]{}|;:,.<>?';

function generatePassword() {
    const length = parseInt(lengthInput.value);
    let charset = '';
    if (includeUppercase.checked) charset += uppercaseChars;
    if (includeLowercase.checked) charset += lowercaseChars;
    if (includeNumbers.checked) charset += numbers;
    if (includeSpecial.checked) charset += specialChars;

    if (charset === '') {
        alert('Please select at least one character type.');
        return;
    }

    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
    }

    passwordField.value = password; 
}

function copyPassword() {
    const password = passwordField.value;
    if (!password) {
        alert('No password to copy!');
        return;
    }

    navigator.clipboard.writeText(password).then(() => {
        alert('Password copied to clipboard!');
    }).catch(err => {
        alert('Failed to copy password: ' + err);
    });
}

function checkPasswordStrength(password) {
    fetch('http://localhost:5000/check-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password }),
    })
    .then(response => response.json())
    .then(data => {
        feedbackDiv.innerHTML = `<p>Strength: ${data.strength}</p>`;
        feedbackDiv.innerHTML += `<ul>${data.feedback.map(fb => `<li>${fb}</li>`).join('')}</ul>`;
    })
    .catch(err => {
        feedbackDiv.innerHTML = '<p>Error checking password strength.</p>';
    });
}

generateBtn.addEventListener('click', generatePassword);
copyBtn.addEventListener('click', copyPassword);
checkBtn.addEventListener('click', () => {
    const password = passwordInput.value;
    checkPasswordStrength(password);
});
