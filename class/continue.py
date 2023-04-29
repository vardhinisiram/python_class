sum  = 0


for i in range(10):
    data = int(input("Enter the "+ str(i+1)+" number: "))
    if data < 0:
        continue
    sum += data

print("The sum of all numbers is ", sum)


    

