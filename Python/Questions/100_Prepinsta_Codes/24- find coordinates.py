# find coordinates

x,y=map(int,list(input('insert the value for x and y :- ').split()))
if x>0 and y>0:
    print('point("x","y") is in first quadrant')
elif x<0 and y>0:
    print('point("x",",y,") is in second quadrant')
elif x<0 and y<0:
    print('point(",x,",",y,") is in third quadrant')
elif x>0 and y<0:
    print('point(",x,",",y,") is in fourth quadrant')
elif x==0 and y==0:
    print('point(",x,",",y,") is in origin')    
elif x==0:
    print('point(",x,",",y,") is in y-axis')    
elif y==0:  
    print('point(",x,",",y,") is in x-axis')
else:
    print('point(",x,",",y,") is in unknown quadrant')