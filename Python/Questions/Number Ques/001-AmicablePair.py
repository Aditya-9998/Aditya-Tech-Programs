# sum of poper divisor of a no amicable  pair
'''
n1,n2=int(input('enter no')),(input('enter no'))

def amicablePair(n1,n2):
    #process
    s1,s2=0,0
    for i in range(1,n1):
        if (n1%i==0):
            s1=s1+i

    for j in range(1,n2):
        if (n2%j==0):
            s2=s2+i

    if (n1==s2 and n2==s1):
        print('amicable freindly pair')#220,284
    else:
        print('not amicable freindly pair')

amicablePair(n1,n2)'''




def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def amicable_pairs(limit):
    return [(num, sum_of_divisors(num)) for num in range(2, limit+1) 
            if sum_of_divisors(num) != num and sum_of_divisors(num) <= limit 
            and sum_of_divisors(sum_of_divisors(num)) == num]

limit = int(input("Enter a limit: "))
print("Amicable pairs:")
print(amicable_pairs(limit))
