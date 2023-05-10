n=int(input())
x=[int(i) for i in input().split()]
y=[int(j) for j in input().split()]
if len(x)+len(y)<n:
    print("oh my keyboard")
else:
    level=len(x)
    for i in y:
        if i not in x:
            level+=1
    if level==n:
        print("i wanna be the guy")
    else:
        print("oh my keyboard")