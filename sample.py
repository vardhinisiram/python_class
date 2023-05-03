with open ('file' ,'r') as f:
    for row in f.readlines():
        x,y=[int(x) for x in row.split()]
        c = x+y
        output = open('output.txt', 'a') 
        output.write(" ".join([str(x), str(y), str(c)]))
        output.write("\n")
