#wap to find longest word in the sentence.
#count char frequency eg how many time char has repeat
#check is Anagram or not
#check given string is palindroms

#ist methode
l=input('enter strning:- ').split()
print(max(l,key=len))
#2nd methode
print(max(input('enter string ').split(),key=len)) #A-65,a-77,H-72,i-105,e-101   max- compare as an assci value
