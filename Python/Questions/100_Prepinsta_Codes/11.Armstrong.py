# Write a Python function to check whether a number is Armstrong number or not.

def armstrong(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)**3
    if sum == int(n):
        return True
    else:
        return False
n = 153
print(armstrong(n))
# Output:
# True
