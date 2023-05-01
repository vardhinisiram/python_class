T=int(input())
for i in range(T):
    x,y=[int(x) for x in input().split()]
    if x==y:
        print("he likes the match")
    if x!=y:
        print("he does'nt like the match")

