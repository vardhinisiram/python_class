T=int(input())
for i in range(T):
    maths,phy,che=[int(x) for x in input().split()]
    a=(maths+phy)/2
    b=(phy+che)/2
    c=(che+maths)/2
    if a<35.0:
        print("fail")
    elif b<35.0:
        print("fail")
    elif c<35.0:
        print("fail")
