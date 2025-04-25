#leap yr or not

yr=int(input('Enter Year:_'))
if (yr%400==0)or(yr%100==0 and yr%4!=0):
 print("leap Year")
else:
 print("Not a leap year")