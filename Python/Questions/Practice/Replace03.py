#replace all ocerance of a given digit with another given digit in a num

def replace_digits():
    
    num = input("Enter a number: ")
    digit_to_replace = input("Enter the digit to replace: ")
    replacement_digit = input("Enter the replacement digit: ")


    if not num.isdigit() or not digit_to_replace.isdigit() or not replacement_digit.isdigit():
        print("Error: Input must be digits only.")
        return

    if len(digit_to_replace) != 1 or len(replacement_digit) != 1:
        print("Error: Digit to replace and replacement digit must be single digits.")
        return
    
    result = num.replace(digit_to_replace, replacement_digit)

    print("Original Number:", num)
    print("Replaced Number:", result)

replace_digits()


'''
4. Replace large prime digit in given no with 0 senod largest with 1 and so on...#98767310..98060110..
'''