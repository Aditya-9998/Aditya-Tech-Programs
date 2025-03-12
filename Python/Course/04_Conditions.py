'''
num1=int(input('enter value:-'))
num2=int(input('Enter value:-'))
opr=input('enter operator,(+,-,*,/):-')

if opr=='+':
    print(num1+num2)
elif opr=='-':    #if opr=='-':
    print(num1-num2)
elif opr=='*':
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print('Invalid operation....')


# FOR - Loop with range:
for i in range(2):
 print('In range fn() st value by deafult 0 and than 5')
print()# for two condition

for i in range(1,3):
 print('if range in two value than first is initlization, last')
print()#for three condition (Increament)

for i in range(1,10,2):
 print(i,'if last one is Increment or Decrement value. ')
print()

#for Decrement
for n in range(5,0,-2):
    print('Aditya',n)

print()# print the 2's Table in real format
print("Table of 2's:- ")
for i in range(1,11):
    print('2*',i,'=',2*i)

# while loops
# how to use (start,condition,increment)

i=0
while i<=10:
    print(i,'Aditya')
    i=i+2 
print(i)

# IN decrement:
a=10
while a>=0:
    print(a,'Adi')
    a=a-3
print(a)

'''