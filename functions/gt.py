def grater(x:int,y:int,z:int)->int:
        #x,y,z=[ int (x) for x in input("enter three values: ").split()]
    big = 0
    if x>y and x>z:
        big = x 
    elif y>z and y>x:
        big = y 
    elif z>x and z>y:
        big = z
    return big

largest=grater(4,6,2)

print(largest) 
