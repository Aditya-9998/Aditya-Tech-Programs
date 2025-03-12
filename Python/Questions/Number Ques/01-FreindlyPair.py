'''
n1,n2=int(input('enter no')),int(input('enter no'))

def friendlyPair(n1,n2):
    s1,s2=0,0
    for i in range (1,n1//2+1):
        if (n1%i==0):
            s1=s1+i
        
    for j in range(1,n2//2+1):
        if (n2%j==0):
            s2=s2+j
    n3=(s1-n1)/n1
    n4=(s2-n2)/n2
    if (n3==n4):
        print('Friendly pair')
    else:
        print("NOt freindly pair")

friendlyPair(n1,n2)
'''
#2nd methode

def abundance(n):
    ans=1
    #process
    for i in range(2,n//2):
        if not n%i:
            ans=ans+i
    return ans/n

n1,n2=int(input('enter no')),int(input('enter no'))
a1=abundance(n1)
a2=abundance(n2)
if a1==a2:
    print('yes')
else:
    print('no')