# Reverse a number
num=int(input('Enter no:-'))
temp=num
rev=0
while num>0:
    r=num%10
    rev=(rev*10)+r
    num=num//10
print('Reverse of',temp,'is',rev)

#num=int(input('Enter no:-'))
#rint('Reverse of',num,'is',int(str(num)[::-1]))