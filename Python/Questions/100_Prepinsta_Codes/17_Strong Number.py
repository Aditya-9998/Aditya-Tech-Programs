# Strong Number

n=25
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("The number is a Strong Number")
else:
    print("The number is not a Strong Number")