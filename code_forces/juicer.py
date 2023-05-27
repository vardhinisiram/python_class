n,b,d=[int(x) for x in input().split()]
a=[int(x) for x in input().split(" ")[:n]]
juicer=0
empty=0
#for i in range(n):
#	a.append(int(input())) 
for i in a:
	if i<=b:
        juicer+=i
	if juicer>=d:
		juicer=0
		empty+=1
print(empty)

