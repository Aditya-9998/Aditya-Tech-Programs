'''

def palindrome_triangle(n):
    # Create the palindrome triangle in a single row
    output = ""
    for i in range(1, n + 1):
        # Generate the increasing part (1 to i)
        for j in range(1, i + 1):
            output += str(j)
        # Generate the decreasing part (i-1 to 1)
        for j in range(i - 1, 0, -1):
            output += str(j)
    print(output)

# Input
n = int(input('Enter aspacts no:- ').strip())
palindrome_triangle(n)

'''
def palindrome_triangle(n):
    for i in range(1, n + 1):
        # Generate the increasing part (1 to i)
        increasing_part = ''.join(str(j) for j in range(1, i + 1))
        # Generate the decreasing part (i-1 to 1)
        decreasing_part = ''.join(str(j) for j in range(i - 1, 0, -1))
        # Combine both parts and print the row
        print(increasing_part + decreasing_part)

# Read input
n = int(input('Enter no').strip())
palindrome_triangle(n)