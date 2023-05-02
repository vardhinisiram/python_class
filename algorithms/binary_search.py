a=[20,25,30,35,40,45]
x=int(input("enter the number: "))
found=False
#while len(a)!=1:
for i in a:
    mid=(0+len(a))//2
    if x==a[mid]:
        print(x," is in the list")
        found=True
        break
    if x>a[mid]:
        a=a[mid:]
    elif x<a[mid]:
        a=a[:mid+1]
if x==a[0]:
    print(x," is in the list")
    found=True
#if len(a) == 1 and a[0] == x:
#        print(x," is in the list")
#        found=True
if found==False:
    print(x," is not in the list")
    


