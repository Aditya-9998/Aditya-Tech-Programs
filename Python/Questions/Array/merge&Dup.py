#a=[12,34,65,78,98,9,98]
#b=[46,78,79,90,45,9,98]
a=list(map(input().split()))
b=list(map(input().split()))
print(list(set(a+b)))

ans=[]
for ele in a+b:
    if ele not in ans:
        ans.append(ele)

print('orderd single line--',list(dict.fromkeys(a+b)))