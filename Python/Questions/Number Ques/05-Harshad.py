#if a no positive no divisble by digit is no called as joy no.def

temp=n=int(input('enter'))
digit=[]

while temp>0:
    digit.insert(0,temp%10)
    temp//=10

print('no' if n%sum(digit) else 'yes')
#readability