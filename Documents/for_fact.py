i=1
a=int(input("enter a number:"))
print("the factors of " ,a, "are :")
for i in range(1,a +1):
    if (a%i==0):
        print(i)
    i=i+1

