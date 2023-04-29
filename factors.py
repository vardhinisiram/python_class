i = 1
a = int(input("enter the number:"))
while i <= a:
    if a%i == 0:
        print(i) 
    if a / 2 <= i:
        break;
    i=i+1
print(a)
print("loop ended")


