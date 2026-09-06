import random

def is_valid_amount(amount):

    return amount > 0


def format_currency(amount):

    return f"₱{amount:,.2f}"

# For Large-Withdrawal OTP

def generate_otp():
    return str(random.randint(100000, 999999))