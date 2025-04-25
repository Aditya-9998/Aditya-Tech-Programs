 # count the days in given yr or month

month=int(input("Enter month 1-12:- "))
yr=int(input("Enter yr:- "))

if ((month==2) and ((year%4==0) or (year%100==0) and (year%400==0))):
     print("The no of days is 29")
elif month==2:
    print("The days is 28")
elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
     print('The count the days are 31')
 
else:
    print("The day count is 30 only")

# test cases 1600,1700,1900 ,2000, 20242