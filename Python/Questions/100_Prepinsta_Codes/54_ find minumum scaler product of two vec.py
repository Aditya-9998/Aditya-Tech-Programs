# find minumum scaler product of two vector

arr1=[1,2,3,4,5,6,7]
arr2=[3,7,7,9,0,46,43,65]
n=len(arr1)

arr1.sort()
arr2.sort(reverse=True)

product=0
for i in range (n):
    product+=arr1[i]*arr2[i]
print(product)