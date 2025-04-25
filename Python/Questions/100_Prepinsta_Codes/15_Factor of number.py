#factor of number

def div(n):
    i=1
    while i<=n:
        if n%i==0:
            print(i,end=' ')
        i+=1
print('The divisor of  is:')
div(n=int(input('Enter the number: ')))