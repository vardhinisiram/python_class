t=int(input())
a,b =[int(x) for x in input().split()]
c=0
while a:
    if a%b==0:
        print(a)
    c+=1
    a+=1
print(c)