t=int(input())
while t != 0:
    a,b =[int(x) for x in input().split()]
    if a == b:
        print(0)
    else:
        print(b - a%b)
    t-=1