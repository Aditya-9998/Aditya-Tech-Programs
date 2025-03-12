'''
race: care 
it all charectars are persent but defferent order.'''

from collections import Counter as C
def isAnagram1(str1,str2):
    return len(str1)==len(str2) and C(str1)==C(str2)

def isAnagrams(str1,str2):
    return len(str1)==len(str2) and sorted(str1)==sorted(str2)

    '''return true or false

    if len(str1)!=len(str2):
        return False
    else:
        sorted(str1)==sorted(str2)
'''

s1,s2=input('Enter1_'),input('Enter_')
print('yes' if isAnagrams(s1,s2) else 'No')