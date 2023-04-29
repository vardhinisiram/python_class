number=int(input("enter the number :"))
if number % 2 == 0:
    print(" the given number is not prime number.")
else: 
    i=3
    a=number//2
    while i<=a:
        if number%i==0:
            print ("the given number is not a prime number")
            exit()
        i=i+1
    print("the given number is a prime number")

