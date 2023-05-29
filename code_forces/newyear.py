t=int(input())
for i in range(t):
    n=int(input())
    num=n//2021
    if n%2020==0:
        print("yes")
    elif n%2020<=num:
        print("yes")
    else:
        print("no")


