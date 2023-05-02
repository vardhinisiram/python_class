"""
T=int(input())
for i in range(T):
    a=[int(x) for x in input().split()]
    remove=0
    for i  in a:
        if i>1000:
            remove+=1
    print(remove)
"""
T=int(input())
N=int(input())
a=[]
a.append(list(input().split(",")))
for i in range(T):
    remove=0
    for i  in a:
        if i>1000:
            remove+=1
    print(remove)

