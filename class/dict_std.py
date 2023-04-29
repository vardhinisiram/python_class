std = {}

name = input("Enter first name ")
std[name] = int(input("Enter the marks: "))

name = input("Enter first name ")
std[name] = int(input("Enter the marks: "))
name = input("Enter first name ")
std[name] = int(input("Enter the marks: "))
name = input("Enter first name ")
std[name] = int(input("Enter the marks: "))




print(std)

average = sum(list(std.values()))/ len(std)

print(average)
