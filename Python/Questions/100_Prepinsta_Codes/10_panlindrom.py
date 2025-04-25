#palindrom
def palindrom(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False
n = 121
print(palindrom(n))
# Output:
# True
# Explanation:  The given number is 121 which is a palindrome number. So the output is True.
# Input:
# 121
# Output:   