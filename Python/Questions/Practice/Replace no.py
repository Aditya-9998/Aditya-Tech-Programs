n=int(input('enter no '))
digit=[]


#sep digit
while n >0:
    r=n%10
    digit.insert(0,r)
    n=n//10#25674
ans=0
small=min(digit)
large=max(digit)
for next_digit in digit:
    if next_digit is small:
        ans=ans*10+large
    else:
        ans=ans*10+next_digit
print(ans)