# Strong number



n=1453544424
temp=n
sum=0
f=[0]*10
f[0]=1
f[1]=1

for i in range (2,10):
    f[i]=f[i-1]*i   
while(temp):
    r=temp%10
    temp=temp//10
    sum+=f[r]
if(n==sum):

    print('yes',n,"Strong number")
else:
    print('no',n,"Strong number")