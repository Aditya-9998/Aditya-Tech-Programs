# Binary to decimal conveter

bin='10001' # Binary number //--17
sum=0
n=len(bin)
for i in range(n):
    sum=sum+int(bin[i])*pow(2,i)
print(sum)