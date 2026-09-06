import random

def is_valid_amount(amount):

    return amount > 0


def format_currency(amount):

    return f"₱{amount:,.2f}"

# For Large-Withdrawal OTP

def generate_otp():
    return str(random.randint(100000, 999999))

"""
######### Learning Signature #########
Programmed by: Elizabeth Maude M. Lara
Date Submitted: September 6, 2026

Program Description: I added a generate_otp() function that produces a random 6-digit code, used to confirm large withdrawals before they go through.
Reflection: I learned how a simple random number generator can simulate a real-world security step like an SMS one-time code.

AI Usage
[ ] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[/] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""