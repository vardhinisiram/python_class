
"""
for j in range(5):
    for i in range(5):
        print(j, i, end = " ")
    print()

print()
"""

n = int(input("enter the number "))
i = 1
while i<=n:
    if i%2 == 0 :  
        i+=1
        continue
    print(i * '* ' )
    i=i+1
n=n-1 
while n!=0:
    if n % 2 == 0:
        n = n-1
        continue
    print(n * '* ')
    n=n-1





