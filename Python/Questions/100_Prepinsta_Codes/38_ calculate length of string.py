# calculate length of string
def len(str):
    if str=="":
        return 0
    return 1+len(str[1:])
str="'Aditya is my name.'"
print('length of',str,'is',len(str))