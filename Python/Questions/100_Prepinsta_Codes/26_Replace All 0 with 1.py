#Replace All zero with one

n=int(input('Enter no:- '))
s=str(n)
l=[]
for i in s:
    if (i=='0'):
        l.append('1')
    else:
        l.append(i)
ns=""
for i in l:
    ns+=i
print("Converted number is",int(ns))