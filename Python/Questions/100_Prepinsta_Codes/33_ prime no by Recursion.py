# prime no by Recursion

def prime(n,i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return prime(n,i+1)
n=int(input('Enter the no:- '))
if prime(n):
    print('Yes',n,'is prime')
else:
    print("No",n,'not prime')