a=[7,5,3,2,4,1]
i=1
while i!=len(a):
    for x in a[:i]:
        if a[i]<a[a.index(x)]:
            H=a[a.index(x)]
            a[a.index(x)]=a[i]
            print(a,x)
            while i!=a[i+1]:
                a[i]=a[i-1]
                i-=1
    i+=1
print(a)