'''

#Immutable DataTypes
#Integer
a=5; print(a,type(a))

#Float
a=5.5; print(a,type(a))

#Complex number
a=3+2j; print(a,type(a))

#string
s='Thhis is string'
s1=''A multi-line string
hello aman
''
print(s,s1, type(s1)) 

t=('adi',4,8,0.5,'anu') #tuple
t1=('anup',)
print(t1,type(t1))
print(t,type(t))
'''

#Mutable DataTypes
l=[6,8,'Aditya','Aman',0.3] #list
print(l,type(l))
l[2]='Anup';print(l,type(l))

d={
'course_name': 'B.tech',
'course_duration':'2 Month'
}#{1:'value','key':2} #dictionary
print(d['course_name'])
print(d,type(d))  
#Example
a={
 'Name':'Sujit Gaur',
'branch':'I.T',
'duration':'4 year'
}
print(type(d),a)
print( a['duration'])

s={1,1,2,4,6,2}#set  
print(s,type(s))
