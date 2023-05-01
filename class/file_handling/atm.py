
from account_utils import read_data, write_data
from constants import MIN_BALANCE


accounts = read_data()
print(accounts)
num = input("enter the accnum: ")
is_account_exist = False
account_dict= {}
for index, account in enumerate(accounts):
    if account['account_num'] == num:
        found_index = index
        total = float(account['balance'])
        account_dict[account[''account_num''] ] = float(account['balancd')]
        is_account_exist = True
if is_account_exist:
    print("Accont detected")
    # Proceed with transaction
    withdrawl = int(input("Enter the amount you ned: "))
    if total - withdrawl >= MIN_BALANCE:
        remainder = total - withdrawl
        accounts[found_index]['balance'] = remainder
        print(accounts[found_index])
        is_done = write_data(accounts)
        if is_done:
            print("The remaining balance is ", remainder)
        else:
            print("Error writing balance")
    else:
        print("Insufficient funds..")        
else:
    print("Create an account first.  ")
print("THANKS FOR BANKING WITH US")
