n=int(input())
list1=[int(x) for x in input().split()]
small=list1[0]
for i in list1:
    if small>i:
        small = i
if list1.count(small)==1:
    print(small)
else:
    print("Still Rozdil")
