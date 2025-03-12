const generateBtn = document.getElementById('generateBtn');
const copyBtn = document.getElementById('copyBtn');
const passwordField = document.getElementById('Password'); // The input field for password
const lengthInput = document.getElementById('length');
const includeUppercase = document.getElementById('includeUppercase');
const includeLowercase = document.getElementById('includeLowercase');
const includeNumbers = document.getElementById('includeNumbers');
const includeSpecial = document.getElementById('includeSpecial');

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

    navigator.clipboard.writeText(password).then(function() {
        alert('Password copied to clipboard!');
    }).catch(function(err) {
        alert('Failed to copy password: ' + err);
    });
}

generateBtn.addEventListener('click', generatePassword);
copyBtn.addEventListener('click', copyPassword);
