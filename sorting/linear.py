a=[10,23,45,6,20]
x=int(input("search the number: "))

"""
while i <= len(a)-1:
    if x==a[i]:
        print("the number is in the list",a[i])
        break 
    i=i+1
"""
for i in a:
    if x==i:
        print("the number is in the list",i)
