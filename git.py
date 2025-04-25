print('Hello Aditya')

# sitting: system>clipbord




'''

🔧 Sahi Tarika (Step-by-step):
✅ Step 1: Ek .gitignore file banao

Terminal ya text editor se:

notepad .gitignore

Isse ek text editor खुल जाएगा. Usme ye content copy-paste karo:

# Sab kuch ignore karo Program folder ke andar
/Program/*

# Lekin in specific folders ko track karo
!/Program/Python/
!/Program/Java/
!/Program/Java Script/
!/Program/Html/
!/Program/DSA/

# Kuch system folders ko ignore karo
/Program/.vscode/
/Program/node_modules/
/Program/Dream-Project/
/Program/Projects/

# Unwanted file types
*.log
*.tmp
*.csv
*.pyc
__pycache__/

Save करके बंद कर दो.
✅ Step 2: Git commands terminal mein run karo:

cd "C:\Users\Aditya Kumar\Acadimic\Program"

git init
git remote add origin https://github.com/Aditya-9998/My-project

git add .gitignore
git add Python/ Java/ "Java Script/" Html/ DSA/

git commit -m "Final selective folders setup"
git branch -M main
git push -u origin main

Ab sirf wahi 5 folders GitHub pe upload honge. Baaki sab Git ignore karega — future mein bhi.



'''