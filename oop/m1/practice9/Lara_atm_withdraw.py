from datetime import datetime
from Lara_atm_account import Account

def withdraw_money(account, amount):
    if amount <= 0:
        return False

    success = account.withdraw(amount)

    if success:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open("transactions.txt", "a") as file:
            file.write(
                f"Timestamp: {timestamp}\n"
            )

            file.write(
                f"Account: {account.account_name}\n"
            )

            file.write(
                f"Transaction: Withdraw\n"
            )

            file.write(
                f"Amount: ₱{amount:.2f}\n\n"
            )

            file.close()
        return True
    return False

account = Account("Elizabeth Maude Lara", 10000.00)
withdraw_money(account, 2000.00)

""" 
######### Learning Signature ######### 
Programmed by: Elizabeth Maude M. Lara
Date Submitted: September 03, 2026
 
Program Description: This program is a ATM command line interface where users can withdraw money from their account and their balance update accordingly.
Reflection: I learned to use object oriented programming in Python, particularly how to manage balance reductions and ensure withdrawal logic works correctly.

AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""