'''
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude other even numbers
    for i in range(3, int(n**0.5) + 1, 2):  # Check only odd numbers up to √n
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
'''
    #2nd method

n = int(input("Enter a number: "))

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print(n, "is not prime.")
        break
else:
    print(n, "is prime.")
    
print(2, int(n**0.5) + 1)
