# N^th row in pascal tringle

def row(n):
    pre=1
    print(pre,end=' ')
    for i in range(1,n+1):
        curr=(pre*(n-i+1)) //i
        print(curr,end=' ')
        pre=curr
n=5
row(n)