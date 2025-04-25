# perfect squre

from math import sqrt
def square(x):
    if x>=0:
        sr=sqrt(x)
        return ((sr*sr)==x)
    return False
n=25
if square(n):
    print("The number is a perfect square")
else:
    print("The number is not a perfect square")