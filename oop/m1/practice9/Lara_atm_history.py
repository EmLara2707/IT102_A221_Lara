def view_history():
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return []

for line in view_history():
    print(line.strip())

""" 
######### Learning Signature ######### 
Programmed by: Elizabeth Maude M. Lara
Date Submitted: September 03, 2026
 
Program Description: This program is a ATM command line interface where users can pull up and view their complete transaction history.
Reflection: I learned to use object oriented programming in Python to organize transaction data and present it properly to the user.

AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""