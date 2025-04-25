# count the even or odd element in given array

a=[2,3,5,78,56,34,7,8,9,2,0,14,16,17,19,3,0,89,65,88]

even=0
odd=0
for i in  a:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("Even no in array list is",even,"odd count is",odd)

#Test cases  check differnt will be ocours in here [3,5,7,8,9,10,11,12,13,14,15,16,17,19]