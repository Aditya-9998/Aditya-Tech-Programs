#wap calulate sumof the adjecant digit of a given positive difference bw two digit regardless of their order you must not convert into string.
'''
n=int(input('enter no:-'))
n=n%10
for n in range(1,n+1):
    s=n+n
    print(n)
print(s)'''

#1nd method

n=int(input('Enter no:-'))
digit=[]
while n>0:
    rem=n%10
    digit.insert(0,rem)
    n=n//10

abs_diff=[]
for i in range(1,len(digit)):
    diff=abs(digit[i]-digit[i-1])
    abs_diff.append(diff)
print(abs_diff)
sum_abs_diff=sum(abs_diff)
print(sum_abs_diff)