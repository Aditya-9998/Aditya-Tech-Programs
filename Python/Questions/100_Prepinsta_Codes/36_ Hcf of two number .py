# Hcf of two number using Recurision

def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a %b)

a1,b1=6556,76867
print('Hcf of ',a1,'and',b1,'is',hcf(a1,b1))