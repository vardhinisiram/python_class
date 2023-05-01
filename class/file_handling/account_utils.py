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
    accounts = {}
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file) 
        for line in reader:
            #print(line)
            accounts[line["account_num"]] = float(line["balance"])

    return accounts


def write_data(accounts_dict):
    """
        This function is used to write the account info to a file given
    """
    file_name = ACCOUNTS_FILE
    header = ['account_num', 'balance']
    final_list = []
    for key, value in accounts_dict.items():
        final_list.append({header[0]:key, header[1]: value})
    
    with open(file_name, 'w') as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(final_list)
    return True


