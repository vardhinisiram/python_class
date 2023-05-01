
from account_utils import read_data, write_data
from constants import MIN_BALANCE


accounts = read_data()

num = input("enter the accnum: ")

if num in accounts:
    print("Accont detected")
    total = accounts[num]
    withdrawl = int(input("Enter the amount you ned: "))

    if total - withdrawl >= MIN_BALANCE:
        # Proceed with transaction
        remainder = total - withdrawl
        accounts[num] = remainder
        is_done = write_data(accounts)
        if is_done:
            print("The remaining balance is ", remainder)
        else:
            print("Error writing balance")
    else:
        print("INSUFFICIENT FUNDS")
else:
    print("Create an account first.  ")
print("THANKS FOR BANKING WITH US")
