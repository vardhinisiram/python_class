a=[20,25,30,35,40,45]
x=int(input("enter the number"))

half=(0+len(a))//2
if x==a[half]:
    print(x,"is in list")
if x>half:
    half=(half+len(a))//2
    if x==half:
        print (x,"in the list")


