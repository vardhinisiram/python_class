a=[1, 34, 55, 123, 455, 677, 888]
half=len(a)//2-1
x=int(input("enter the number: "))
i=0
if x <= a[half]:
    while i<=half:
        if x==a[i]:
            print(x, "is in the list")
            break
        i=i+1
        
elif x >= a[half]:
    i=half
    while i <= len(a)-1:
        if x==a[i]:
            print(x, "is in the list")
        i=i+1
