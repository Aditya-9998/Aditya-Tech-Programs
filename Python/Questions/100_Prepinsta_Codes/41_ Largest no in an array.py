# Largest no in an array

a=[56,87,98,909,23,45,00]
a.sort()
print(a[-1],'First methode')

a=[56,87,98,909,23,45,00]
print(max(a),'Second Method')

a=[56,87,98,909,23,45,00]
max=a[0]
for i in range (len(a)):
    if a[i]>max:
        max=a[i]
print(max,'Third method')