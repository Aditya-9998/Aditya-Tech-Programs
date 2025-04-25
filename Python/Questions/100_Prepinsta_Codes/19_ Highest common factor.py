# Highest common factor

n1,n2=30,45
hcf=1
for i in range(1,min(n1,n2)):
    if n1%i==0 and n2%i==0:
        hcf=i
print('hcf of ',n1,' and ',n2,' is ',hcf)
