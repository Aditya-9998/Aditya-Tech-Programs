def left_rotate_string(s,n):
    #n=n%len(s)
    return s[n:]+s[:n]

def right_rotate_from(s,n):
    #n=n%len(s)
    return s[-n:]+s[:-n]
s='hello'
left=left_rotate_string(s,2)
right=right_rotate_from(s,2)
print('left part',left)
print('right part is',right)