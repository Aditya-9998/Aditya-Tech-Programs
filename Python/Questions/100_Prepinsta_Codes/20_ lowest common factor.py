# lowest common factor

n1=4
n2=8
for i in range(1,max(n1,n2)):
    if n1%i==n2%i==0:
        hcf=i

lcm=(n1*n2)//hcf
print("LCM of",n1,"and",n2,"is",lcm)
