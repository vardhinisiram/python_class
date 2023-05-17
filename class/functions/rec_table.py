def table(n, i):
    if i == 10:
        val = str(n)+" * "+str(i)+" = "+str(n*i)
        print(val)
    else:
        print(n, "*", i, "= ", n*i)
        print("open ", i)
        table(n, i+1)
        print("close ", i)
table(5,1)
