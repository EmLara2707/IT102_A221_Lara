class Account:
    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance
    
    def check_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

""" 
######### Learning Signature ######### 
Programmed by: Elizabeth Maude M. Lara
Date Submitted: September 02, 2026
 
Program Description: This program is a ATM command line interface where account holders can view their current balance, add money to their account, and take money out.
Reflection: I learned to write a class to hold account data and methods for deposits and withdrawals, which made the code easier to organize and expand.
 
AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""