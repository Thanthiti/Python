x = 60
y = 0
z = 0
if(x >= 60): 
    print('1')
    y = z = 0 
    x +=3
    if(x <= 60):
        print('2')
        y = x
        z = 0 
    else: 
        print('3')
        y = x-10 
        if( y > 60):
            print('4')
            z = y 
        else:
            print('5')   
            z=y+10
print(x,y,z) 
        
