# calculate no of digit in an integer

n=int(input('Enter int:- '))
print(len(str(n)))

#using function
def digit(n):
    count=0
    while n!=0:
        n//=10
        count+=1
    return count
n=int(input('Enter digit:- '))
print("Entered digits : %d"%(digit(n)))