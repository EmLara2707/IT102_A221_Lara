""" 
######### Learning Signature ######### 
Programmed by: Elizabeth Maude M. Lara
Date Submitted: September 04, 2026
 
Program Description: This program is a simple ATM web interface created using Streamlit and offers users a full set of banking options.
Reflection: I learned to use Streamlit to design a user friendly front end, bringing together multiple features and connect a graphical interface with the underlying backend logic.

AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""

import streamlit as st

from Lara_atm_account import Account
import Lara_atm_balance
import Lara_atm_deposit
import Lara_atm_withdraw
import Lara_atm_history
import Lara_atm_analysis

account = Account(
    "Juan Dela Cruz",
    10000.00
)

st.set_page_config(
    page_title = "Python ATM",
    page_icon = "🏦",
    layout="wide"
)

st.title("PYTHON ATM")

st.write(
    f"Welcome, **{account.account_name}**!"
)

st.divider()

st.sidebar.title("ATM MENU")

choice = st.sidebar.radio(
    "Select an option:",
    [
        "Check Balance",
        "Deposit",
        "Withdraw",
        "View History",
        "Analyze Transactions"
    ]
)