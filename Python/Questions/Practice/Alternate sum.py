
'''
# 1st methode.
n=int(input("Enter no "))
os, es =0,0
temp=n; pos=1
while temp>0:
    digit=temp%10
    if pos&1: #pos%2==1 
        os+=digit
    else:
        es+=digit
    temp=temp//10
    pos+=1
print(os-es)

print(-11%4 ) # % means remindar Example:

#Second method by string.

n=input("enter no ")
os,es=0,0
for i,digit in enumerate(n[: :-1],1):
    if i%2==1:
        os+=int(digit)
    else:
        es+=int(digit)

print(os-es)

22 oct 2024
concept:-

modules
bitwise
string
enumrate
flot or divison
slicing
list

'''
#3rd way to do:

n=input('Enter no ')[::-1]
osStr,esStr=n[: :2] ,0
for digit in osStr:
    osStr+=int(digit)
es=[int(digit) for digit in esStr]

print(osStr,sum(esStr))

