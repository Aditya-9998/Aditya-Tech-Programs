# first half in asscending then decending
arr=[3,4,5,6,5,5,0,68,1,8787,878,36,57,372,39]
arr=sorted(arr)
print(arr)
l=arr[int(len(arr)/2):]
arr[int(len(arr)/2):]=reversed(l)
print(arr,len(arr))