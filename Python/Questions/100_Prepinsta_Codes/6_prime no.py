# prime no
n=int(input('Enter no'))
count=0
for i in range(2,n):
 if n%i==0:
  count+=1
  break
if count==1:
 print('Not Prime')
else:
 print('Prime')