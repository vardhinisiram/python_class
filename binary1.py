a=[20,25,30,35,40,45]
x=int(input("enter the number: "))
found=True
while len(a)!=1:
    mid=(0+len(a))//2
    if x==a[mid]:
        print(x," is in the list")
        break
    found=False
    if x>a[mid]:
        a=a[mid:]
    elif x<a[mid]:
        a=a[:mid]
if found==False:
    print(x," is not in the list")
    


