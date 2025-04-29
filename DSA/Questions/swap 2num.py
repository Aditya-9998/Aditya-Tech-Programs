# swap three no using 3 methode

# 1. using third variable
def swap(a, b):
    print("Before swapping: a =", a, ", b =", b)
    temp = a
    a = b
    b = temp
    print("After swapping: a =", a, ", b =", b)
# 2. using arithmetic operation
def swap(a, b):
    print("Before swapping: a =", a, ", b =", b)
    a = a + b
    b = a - b
    a = a - b
    print("After swapping: a =", a, ", b =", b)
# 3. using bitwise XOR
def swap(a, b):
    print("Before swapping: a =", a, ", b =", b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping: a =", a, ", b =", b)