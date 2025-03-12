Duplicate=input("enter string- ")
s=set()
l=[]
for i in Duplicate:
    if s.__contains__(i):
        continue
    else:
        s.add(i)
        l.append(i)
l=''.join(i)
print(l)

'''
str-=input()
ans=''

for i in str-:
    if i not in ans:
        ans=ans+i
print(ans)
'''
