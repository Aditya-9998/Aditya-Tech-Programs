def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    return n == sum(int(d)**num_digits for d in num_str)

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")



'''
def dseprate(n):
    d=[]
    while n>0:
        d.insert(0,n%10)
        n//=10
    return d
    '''