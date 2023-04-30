MIN_BALANCE = 500
ACC_NUMS=[10, 11, 12, 13, 14, 15]

num = int(input("enter the accnum: "))

if num in ACC_NUMS:
    print("Accont detected")
    total = int(input("Enter the total amount: "))
    withdrawl = int(input("Enter the amount you ned: "))

    if total - withdrawl >= MIN_BALANCE:
        # Proceed with transaction
        remainder = total - withdrawl
        print("The remaining balance is ", remainder)

    else:
        print("INSUFFICIENT FUNDS")
else:
    print("Create an account first.  ")
print("THANKS FOR BANKING WITH US")
