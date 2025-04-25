def miniMaxSum(arr):
    # Sort the array
    arr.sort()
    
    # Calculate minimum sum (first 4 elements) and maximum sum (last 4 elements)
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    
    # Print the result
    print(min_sum, max_sum)

# Example Usage
arr = [1, 3, 5, 7, 9]
miniMaxSum(arr)