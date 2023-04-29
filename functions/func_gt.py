def grater(x,y,z):
        #x,y,z=[ int (x) for x in input("enter three values: ").split()]
    if x>y and x>z:
         print(x, "is bigger")
    elif y>z and y>x:
         print(y, "is bigger")
    elif z>x and z>y:
         print(z, "is bigger")
    return 0

largest=grater(4,6,2)

print(largest) 
