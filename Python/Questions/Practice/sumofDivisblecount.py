# wap the given no is count how many is divisble by 3 and 5 and sum the abslute count

n=int(input('Enter no:-'))
c3,c5=0,0
while n>0:
    digit=n%10
    if digit%3==0:
        c3+=1
    elif digit%5==0:
        c5+=1
    n=n//10
print(abs(c5-c3))

#wap coustom fdabo sequnece strting give two from user given no.