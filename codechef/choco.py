T=int(input())
for i in range(T):
    gift,mychoco,cost=[int(x) for x in input().split()]
    x=gift-mychoco
    spend=cost*x
    print(spend)
