# Factorial using recursion

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
number=5
print("Factorial of ",number,'is',fact(number))