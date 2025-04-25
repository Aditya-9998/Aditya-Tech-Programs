
#Factorial of a number

n=6
fac=1
if n<0:
    print('Not possible')
else:
    for i in range(1,n+1):
        fac=fac*i
    print(fac)