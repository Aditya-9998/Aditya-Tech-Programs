#Greatest common divisor
n1=56
n2=87

a=n1
b=n2
while n1!=n2:
    if n1>n2:
        n1=n1-n2
    else:
        n2=n2-n1
print("GCD is",a,'and',b,'is',n1)
