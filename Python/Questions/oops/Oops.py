def fun(x):
    if x>1:
        fun(x//2) 
# Recursion
        fun(x//2)
    print(x)
fun(4)