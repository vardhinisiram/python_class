T=int(input("enter the no.of testcases"))
        
for i in range(T):
    following,followers=[int(x) for x in input().split()]
    
    followers*=10
    if following > followers:
        print ("the account is spam ")
    else:
        print("the account is not spam")
