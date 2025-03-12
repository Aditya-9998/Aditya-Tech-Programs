'''
Python is an interpreted object-oriented high-level programming language with dynamic semantics. 
Introduced by the Guido Van Rossum in 1994. 
It support oops concept, High-level programming Language with Dynamic Semantics.

if A code of 5 lines an error in line 4 than, print output of 4 line than shows error in line no 5.
It show Interpreted property.  '''

print('Hello Aditya!', 2*3,2*2,2*1,2*0,'^ 123'  ,' 1')
a='Raj' ; print('Hello Aditya!',a  ,'2'); print('Arya Aditya',  ' 3')


a=10;b=7 #E.g.
print(a,b) #a=10;b=10 it have same address
print(id(a),id(b))
_a=22;print(_a)

#String Concatatination:-
a='Aditya'
b='Raj'
print(a+' '+b)

#operator in Python
a=25
b=50
print('Operators_',a%4)
print(a/b)
print(a*b)
print(a-b)
print(a+b)
print(a**2), # it help in find exponent of the value 
print(a//4)  #it gives only intger value either skip decimal values   
print(7%2) #it modulas use find remainder

#Assignment operator:-
x=5
print(x)
x+=5
print(x)
print(x-2)

#comaparison operator:-
x=10
y=20
print(x==y)
print(x<=y)
print(x>=y)
print(x!=y) 

#Logical operator
x=10;y=20
print(x==10 and x==y);print(x==10 and x<y)
print(x==y or y==20)
print(x!=10)
print(not x!=10)

#Membership operator:-
h='hello'
print('h' in h)
h1='Hello'
print('Hel' in h1)
print('oo' not in h1);print('oo' in h1)

l=[10,20,30,40,50]
print(50 in l);print(1 in l)  

#Identity Operator
x=10;y=10
print(x is y,x==y)
print(x is not y,x!=y)  

#Bitwise Operator:-
x=10;y=8
print(bin(x))
print(bin(y))
print(x&y,bin(x&y))  #& 1000__8
print(x|y,bin(x|y))  #&  1010__10
print(x^y,bin(x^y))  #^ 0010___2