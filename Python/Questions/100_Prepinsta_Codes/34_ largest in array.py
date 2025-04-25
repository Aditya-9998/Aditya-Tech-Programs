# largest in array

def largest(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1],largest(arr,n-1))

if __name__=="__main__":
    arr=[34,67,4,9,0,223,43435]
    n=len(arr)
    print(largest(arr,n))
