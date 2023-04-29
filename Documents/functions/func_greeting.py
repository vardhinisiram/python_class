def greeting(name,time):
    
    if time >=5 and time < 12:
        print("Good morning" , name)
    elif time >=12 and time < 16:
        print("Good afternoon" , name)
    elif time >=16 and time < 19:
        print("Good evening" , name)
    elif time >=19 and time < 5:
        print("Good night" , name)
    return 


mess=greeting("usha",6)
print(mess)
