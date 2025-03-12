ans={}
string=input()
for char in set (string):
    ans[char]=string.count(char)
for char in string:
    ans[char]=ans.get(char,0)+1

#import collection
from collections import Counter as c
print(c(string))