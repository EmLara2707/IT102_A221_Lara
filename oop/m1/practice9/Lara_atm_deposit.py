from datetime import datetime
from Lara_atm_account import Account

def deposit_money(account, amount):
    if amount <= 0:
        return False

    success = account.deposit(amount)

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
                f"Transaction: Deposit\n"
            )

            file.write(
                f"Amount: ₱{amount:.2f}\n\n"
            )

            file.close()
        return True
    return False

""" 
######### Learning Signature ######### 
Programmed by: Elizabeth Maude M. Lara
Date Submitted: September 03, 2026
 
Program Description: This program is a ATM command line interface where users can add money to their account through a deposit feature.
Reflection: I learned to apply object oriented programming to build basic banking tasks in Python, focusing on how methods inside a class can handle changes to account data.

AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""