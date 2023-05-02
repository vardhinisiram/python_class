"""
amount=int(input("enter the amount :"))
note=int(input("enter the note : "))
print("no.of " ,note," notes",amount//note)
print("change :",amount-(amount//note)*note)
"""
amount=int(input())
c=[50,20,10,1]
a=[]
for i in c:
    if amount//i>0:
        a.append(amount//i)
        
        
print(a)
small=a[0]
i=0
while i<len(a):
    if small>a[i]:
        small=a[i]
    i=i+1
print(small)
