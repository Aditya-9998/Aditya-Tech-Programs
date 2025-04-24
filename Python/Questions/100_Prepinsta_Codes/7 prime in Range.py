# prime no in range  1 to 80
st,en=50,266

prime=[]
for i in range (st,en+1):   
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
print(len(prime),'count of prime no')

# test cases 59 to 80, 15999 to 16999