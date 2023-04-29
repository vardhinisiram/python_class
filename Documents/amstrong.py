num = int(input("enter the number :"))
digit = num
n = len(str(num))
c = 0
while num != 0:
    i = num % 10
    c += i**n
    num //= 10
if c == digit:
    print(digit,"is an amstrong number")
else:
    print(digit, "is not an amstrong number")

    
