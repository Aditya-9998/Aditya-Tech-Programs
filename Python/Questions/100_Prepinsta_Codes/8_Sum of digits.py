# Sum of digits
num=int(input('Enter no:-'))
sum=0
while num!=0:
    d=int(num%10)
    sum=sum+d
    num=num/10
print(sum)