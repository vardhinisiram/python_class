"""
    This file contains utils for handling accounts..
"""

import csv

from constants import ACCOUNTS_FILE

def read_data():
    """
    read_data is used to read the acccount details from given file

    :return: returns the dict with account details.
    :rtype: dict
    """
    file_name = ACCOUNTS_FILE
    accounts_list = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file) 
        for line in reader:
            #print(line)
            accounts_list.append(line)

    return accounts_list


def write_data(accounts_list):
    """
        This function is used to write the account info to a file given
    """
    file_name = ACCOUNTS_FILE
    header = ['account_num', 'balance']
    
    with open(file_name, 'w') as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(accounts_list)
    return True


