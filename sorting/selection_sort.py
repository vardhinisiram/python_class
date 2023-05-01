a=[int(x) for x in input().split()]
b=[]
while len(a)!=0:
	small=a[0]
	i=0
	while i<len(a):
		if small>a[i]:
			small=a[i]
		i=i+1
	a.remove(small)
	b.append(small)
	
print(b)
