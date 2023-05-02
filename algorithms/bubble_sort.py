n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
#a=[15,11,35,29,74,42]
for _ in range(n-1):
    i=0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            e=a[i+1]
            a[i+1]=a[i]
            a[i]=e
        i=i+1
print(a)
