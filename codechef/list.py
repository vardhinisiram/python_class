T=int(input())
for i in range(T):
    a=[int(x) for x in input().split()]
    remove=0
    for i  in a:
        if i>1000:
            remove+=1
    print(remove)
