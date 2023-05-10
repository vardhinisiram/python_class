n,m=[int(x) for x in input().split()]

i=1
while i<=n:
    if i%2!=0:
        print(m*"#")
    elif i%2==0 and i%4!=0:
        print((m-1)*".","#",sep="")
    else:
        print("#",(m-1)*".",sep="")
    i+=1
