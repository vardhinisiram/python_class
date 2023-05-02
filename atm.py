MIN_BALANCE = 500
ACCS = {10:1500,20:5000,30:4000}

num = int(input("enter the accnum: "))
if num not in ACCS.keys():
    exit()
if num in ACCS.keys():
    
    print("Accont detected")
    total = ACCS[num]
    print("the total amount you have: ", total)
    withdrawl = int(input("Enter the amount you ned: "))

    if total - withdrawl >= MIN_BALANCE:
        # Proceed with transaction
        remainder = total - withdrawl 

        print("The remaining balance is ", remainder)

        ACCS.update({num:remainder})
        print(ACCS)
    else:
        print("INSUFFICIENT FUNDS")
else:

    print("Create an account first.  ")
print("THANKS FOR BANKING WITH US")
