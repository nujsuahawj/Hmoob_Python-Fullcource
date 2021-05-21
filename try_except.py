#x=int(input('x='))
#y=int(input('y='))
#z=x/y
#print(z)
try:
    x=int(input('x='))
    y=int(input('y='))
    z=x/y
    #print(z)
except:
    print('yuam kev lawm os ')  
try:
    x=int(input('x='))
    y=int(input('y='))
    if x==0:
        raise Exception()
    z=x/y
    print(z)
except:
    print('yuam kev lawm os ')       