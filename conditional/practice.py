T=int(input("enter the testcases :"))
for i in range(T):
    setter,tester,editor=[int(x) for x in input().split()]
    if (setter>editor) and (setter>tester):
        print("SETTER")
    elif (tester>editor) and (tester>setter):
        print("TESTER")
    elif (editor>tester) and (editor>setter):
        print("EDITOR")
