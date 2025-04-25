'''
Replace prime no 
largest with 01
second largest 2
....

store them in list
return then list
'''

def separate_digits(num):
    
    digits=[]
    return digits

n=int(input('Enter num:-'))
digits=separate_digits(n)
prime_digits=[2,3,5,7]
ans=0
common=list(set(digits).intersection(set(prime_digits)))
common.sort(reverse=True)

for digit in digits:
    if digit in common:
        ans=ans*10+common.index(digit)
    else:
        ans=ans*10+digit
    print(ans)

print(ans)