'''

a=input('Enter no:-') #we put all into in int,flot,eval 
b=input('Enter no:-')  # e.g a=eval(input('enter no'))
print(a,b,type(a),type(b),a+b)

#if statement 
a=int(input("Enter no:-"))
if a%2==0:
    print(a,'even no')
else:
    print(a,'Odd no')

# if & else & elif statement
a=int(input('Enter no:-'))
if a>=60:
    print('First Divison')
elif a>=50:
    print("Second Divison")
elif a>=30:
    print('Third Divison')
elif a>=0:
    print("Third Divison")
else:
    print('WRONG INPUT')
'''    
#string

s='Aditya is my collage name'
l=len(s)
print(l)

print(s[2])
print(s[8])

print(s)