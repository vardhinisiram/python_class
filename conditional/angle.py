a = float(input("enter first number"))
b = float(input("enter second number"))
c = float(input("enter third number"))
if (a==b) and (b==c) and (c==a):
    print("this is eqilateral triangle")
if ((a==b)and(c!=a))or((b==c)and(a!=b)) or ((c==a)and(b!=c)):
    print("this is isoseles triangle")
if (a!=b) and (b!=c) and (c!=a):
    print("this is scalence triangle")
