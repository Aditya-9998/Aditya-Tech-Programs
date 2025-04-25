# Repating elementts in array


def count(arr, n):
    mp = dict()

    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        if mp[x]!=1 :
          print(x)
arr = [10, 30, 40, 20, 10, 20, 50, 10] 
n = len(arr) 
count(arr, n)