num = int(input("enter the number :"))
number=num
cons = 10
f = 0
while number !=0:
    b = number % cons
    f *= cons
    f += b
    number //= cons
if f == num:
    print("given number ",num,"is a palindrome")
else:
    print("given number ",num," is not a palindrome")
   
