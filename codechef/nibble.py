T=3
for i in range(T):
    n=int(input("enter the size in bits: "))
    x=n%4
    if x==0:
        print("GOOD")
    if x!=0:
        print("NOT GOOD")
