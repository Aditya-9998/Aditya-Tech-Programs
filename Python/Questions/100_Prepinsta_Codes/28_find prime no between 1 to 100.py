#find prime no between 1 to 100


st,end=0,100
prime=[]

for i in range (st,end+1):
    c=0
    if i<2:
        continue
    if i==2:
        prime.append(2)
        continue
    for n in range(2,i):
        if i%n==0:
            c=1
            break
    if c==0:
        prime.append(i)

print(prime)