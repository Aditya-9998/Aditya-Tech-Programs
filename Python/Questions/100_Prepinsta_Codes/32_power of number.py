#power of number

def pow(a,b):
    ans=a  
    for i in range(b-1):
        ans=a*ans
    return ans
a=2
b=3
print(a,'to the power',b,'is',pow(a,b)) #print(pow(3,2))
