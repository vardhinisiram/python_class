
i = 1 # initialisation...
n = int(input("Enter the range"))

while i <= n: # condition...
    if i % 2 == 0:
        print(i, n, end = " * ", sep = " | ")
    i = i + 1 # updation......
    # i = n + 1 wrong updation...
print()
