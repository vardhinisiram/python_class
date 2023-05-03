with open ('file' ,'r') as f:
        val=f.readline().split( )
        x,y=[int(x) for x in val]
        c = x+y
        print(x ,y ,c)
