# Replace all even digit with 0 and odd with 1
#1st Methode

def replace_even_odd():
        num = input("Enter a number: ")
        result = ''.join('0' if int(digit) % 2 == 0 else '1' for digit in num)
        
        print("Replaced Number:", result)
replace_even_odd()
