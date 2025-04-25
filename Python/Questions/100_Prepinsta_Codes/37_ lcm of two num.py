# lcm using REcursion

def hcf(a,b):
    if b==0:
        return a
    else:      
        return hcf (b,a%b)

def lcm(a,b):
    return (a*b) //hcf(a,b)

a1=23
b1=69
print('Lcm of',a1,'and',b1,'is',lcm(a1,b1))