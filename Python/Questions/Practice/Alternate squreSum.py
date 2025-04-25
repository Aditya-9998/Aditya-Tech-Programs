# Alternate sum of squres in diffrenece of it.
#1st methode
'''
n=int(input('enter no :- ')) #1234
x=[]; y=[] 

while n>0:
    x.append((n%10)**2)
    n=n//10
for index in range(len(x)-1,-1,-1):
    y.append(x[index])

ans=0
pos=1
for num in y:
    if pos&1:
        ans=ans+num
        print (ans)
    else:
        ans=ans-num
        print(ans)
pos+=1

print(y)
'''

#2nd methode

n=int(input('Enter no:- '))
l=[]

while n>0:
    l.insert(0,(n%10)**2)
    n//=10 #n=n//10
pos=1;ans=0
for digit in l:
    ans=ans+digit if pos&1 else ans-digit
    pos=pos+1

    if pos&1:
        ans=ans+digit
print(l)
print(ans)