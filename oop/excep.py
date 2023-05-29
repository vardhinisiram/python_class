try:
    first=int(input())
    second= int(input())
    if second % 2 != 0:
        raise Exception
    result=first*second
    print(result)
except Exception:
    print("given second input is decreased by one")
    second-=1
    result=first*second
    print(result)

