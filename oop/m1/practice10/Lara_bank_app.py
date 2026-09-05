import streamlit as st

import Lara_bank_auth
import Lara_bank_storage
import Lara_bank_transactions
import Lara_bank_analysis
import Lara_bank_utils


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Lara Bank | Your Trusted Digital Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# IMPROVED CUSTOM GUI
# ==========================================

st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
 
        :root {
            --lb-navy-900: #0B1F3A;
            --lb-navy-700: #14345C;
            --lb-navy-500: #1F4B7A;
            --lb-gold-500: #C6A15B;
            --lb-gold-600: #B08D46;
            --lb-bg: #F4F6F9;
            --lb-card: #FFFFFF;
            --lb-border: #E2E6ED;
            --lb-text: #1C2333;
            --lb-text-muted: #5B6472;
            --lb-success: #1F8A55;
            --lb-danger: #C0392B;
        }
 
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: var(--lb-text);
        }
 
        h1, h2, h3, h4 {
            font-family: 'Libre Franklin', sans-serif;
            font-weight: 700;
            color: var(--lb-navy-900);
        }
 
        .stApp {
            background-color: var(--lb-bg);
        }
 
        /* ---- Top brand banner ---- */
        .lb-banner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(90deg, var(--lb-navy-900), var(--lb-navy-700));
            padding: 22px 32px;
            border-radius: 12px;
            margin-bottom: 22px;
            border-bottom: 3px solid var(--lb-gold-500);
        }
 
        .lb-banner-title {
            font-family: 'Libre Franklin', sans-serif;
            font-weight: 800;
            font-size: 28px;
            color: #FFFFFF;
            margin: 0;
        }
 
        .lb-banner-sub {
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: #C9D3E0;
            margin-top: 2px;
        }
 
        .lb-banner-badge {
            background-color: rgba(198, 161, 91, 0.15);
            border: 1px solid var(--lb-gold-500);
            color: var(--lb-gold-500);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }
 
        /* ---- Sidebar ---- */
        section[data-testid="stSidebar"] {
            background-color: var(--lb-navy-900);
        }
 
        section[data-testid="stSidebar"] * {
            color: #EDEFF4 !important;
        }
 
        section[data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.15);
        }
 
        .lb-sidebar-name {
            font-family: 'Libre Franklin', sans-serif;
            font-weight: 700;
            font-size: 18px;
            margin-bottom: 0px;
        }
 
        .lb-sidebar-balance-card {
            background-color: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 10px;
            padding: 14px;
            margin: 10px 0 16px 0;
        }
 
        .lb-sidebar-balance-label {
            font-size: 11px;
            letter-spacing: 0.3px;
            color: #9FB0C7 !important;
        }
 
        .lb-sidebar-balance-value {
            font-size: 22px;
            font-weight: 700;
            color: var(--lb-gold-500) !important;
        }
 
        .lb-pill {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
            background-color: rgba(198, 161, 91, 0.2);
            color: var(--lb-gold-500) !important;
            border: 1px solid var(--lb-gold-500);
        }
 
        /* ---- Buttons ---- */
        .stButton > button {
            background-color: var(--lb-navy-900);
            color: #FFFFFF;
            border: none;
            border-radius: 8px;
            padding: 10px 18px;
            font-weight: 600;
            transition: background-color 0.15s ease-in-out;
        }
 
        .stButton > button:hover {
            background-color: var(--lb-gold-600);
            color: #FFFFFF;
        }
 
        section[data-testid="stSidebar"] .stButton > button {
            background-color: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.25);
        }
 
        section[data-testid="stSidebar"] .stButton > button:hover {
            background-color: var(--lb-gold-500);
            border-color: var(--lb-gold-500);
        }
 
        /* ---- Inputs ---- */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            border-radius: 8px;
            border: 1px solid var(--lb-border);
        }
 
        /* ---- Metric cards ---- */
        div[data-testid="stMetric"] {
            background-color: var(--lb-card);
            border: 1px solid var(--lb-border);
            border-radius: 12px;
            padding: 16px 18px;
            box-shadow: 0 1px 3px rgba(11, 31, 58, 0.06);
        }
 
        div[data-testid="stMetricLabel"] {
            color: var(--lb-text-muted) !important;
            font-size: 13px;
        }
 
        div[data-testid="stMetricValue"] {
            color: var(--lb-navy-900) !important;
            font-family: 'Libre Franklin', sans-serif;
        }
 
        /* ---- Section card wrapper ---- */
        .lb-section-card {
            background-color: var(--lb-card);
            border: 1px solid var(--lb-border);
            border-radius: 12px;
            padding: 24px 26px;
            margin-bottom: 18px;
            box-shadow: 0 1px 3px rgba(11, 31, 58, 0.05);
        }
 
        .lb-divider-gold {
            height: 3px;
            width: 56px;
            background-color: var(--lb-gold-500);
            border-radius: 2px;
            margin: 6px 0 18px 0;
        }
 
        /* ---- Tabs ---- */
        button[data-baseweb="tab"] {
            font-weight: 600;
        }
 
        /* ---- Dataframe ---- */
        div[data-testid="stDataFrame"] {
            border: 1px solid var(--lb-border);
            border-radius: 10px;
            overflow: hidden;
        }
 
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "account" not in st.session_state:

    st.session_state.account = None

MENU_OPTIONS = [
    "🏠  Dashboard",
    "💵  Deposit",
    "🏧  Withdraw",
    "📜  Transaction History",
    "📊  Transaction Analysis"
]

if "menu" not in st.session_state:
    st.session_state.men = MENU_OPTIONS[0]

# ==========================================
# BANK HEADER
# ==========================================

st.title("Lara Bank")

st.caption(
    "Secure Digital Banking System"
)


# ==========================================
# LOGIN / REGISTRATION
# ==========================================

if not st.session_state.logged_in:

    login_tab, register_tab = st.tabs(
        [
            "Login",
            "Register"
        ]
    )


    # ======================================
    # LOGIN
    # ======================================

    with login_tab:

        st.subheader(
            "Welcome Back"
        )

        account_number = st.text_input(
            "Account Number",
            key="login_account"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="login_pin"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            account, message = (
                Lara_bank_auth
                .login_account(
                    account_number,
                    pin
                )
            )

            if account is not None:

                st.session_state.logged_in = True

                st.session_state.account = (
                    account
                )

                st.success(message)

                st.rerun()

            else:

                st.error(message)


    # ======================================
    # REGISTRATION
    # ======================================

    with register_tab:

        st.subheader(
            "Create Your balaman Bank Account"
        )

        name = st.text_input(
            "Full Name",
            key="register_name"
        )

        account_number = st.text_input(
            "Account Number",
            key="register_account"
        )

        pin = st.text_input(
            "Create 4-Digit PIN",
            type="password",
            key="register_pin"
        )

        confirm_pin = st.text_input(
            "Confirm PIN",
            type="password",
            key="register_confirm_pin"
        )

        account_type = st.selectbox(
            "Account Type",
            [
                "Savings Account",
                "Student Account"
            ]
        )

        starting_balance = st.number_input(
            "Starting Balance",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            account, message = (
                Lara_bank_auth
                .register_account(
                    name,
                    account_number,
                    pin,
                    confirm_pin,
                    account_type,
                    starting_balance
                )
            )

            if account is not None:

                st.success(message)

                st.info(
                    "Your account has been created. "
                    "Please use the Login tab."
                )

            else:

                st.error(message)


# ==========================================
# LOGGED-IN BANKING APPLICATION
# ==========================================

else:

    account = (
        st.session_state.account
    )


    # ======================================
    # SIDEBAR
    # ======================================

    st.sidebar.title(
        "balaman BANK"
    )

    st.sidebar.write(
        f"**{account.account_name}**"
    )

    st.sidebar.caption(
        account.get_account_type()
    )

    st.sidebar.write(
        f"Account: "
        f"{account.account_number}"
    )

    st.sidebar.divider()


    menu = st.sidebar.radio(
        "BANKING MENU",
        [
            "Dashboard",
            "Deposit",
            "Withdraw",
            "Transaction History",
            "Transaction Analysis"
        ]
    )


    st.sidebar.divider()


    if st.sidebar.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.account = None

        st.rerun()


    # ======================================
    # DASHBOARD
    # ======================================

    if menu == "Dashboard":

        st.header(
            f"Welcome, {account.account_name}"
        )

        st.subheader(
            "Account Overview"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Current Balance",
            Lara_bank_utils
            .format_currency(
                account.check_balance()
            )
        )


        col2.metric(
            "Account Type",
            account.get_account_type()
        )


        col3.metric(
            "Account Number",
            account.account_number
        )


        st.divider()


        st.info(
            "Select a banking service from "
            "the menu on the left."
        )


    # ======================================
    # DEPOSIT
    # ======================================

    elif menu == "Deposit":

        st.header(
            "Deposit Money"
        )

        st.write(
            f"Current Balance: "
            f"**{Lara_bank_utils.format_currency(account.check_balance())}**"
        )

        amount = st.number_input(
            "Deposit Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )


        if st.button(
            "Confirm Deposit",
            use_container_width=True
        ):

            if not Lara_bank_utils.is_valid_amount(
                amount
            ):

                st.error(
                    "Invalid deposit amount."
                )

            else:

                success = account.deposit(
                    amount
                )

                if success:

                    Lara_bank_storage.update_account(
                        account
                    )

                    Lara_bank_transactions.record_transaction(
                        account,
                        "Deposit",
                        amount
                    )

                    st.success(
                        "Deposit successful."
                    )

                    st.metric(
                        "New Balance",
                        Lara_bank_utils
                        .format_currency(
                            account.check_balance()
                        )
                    )


    # ======================================
    # WITHDRAW
    # ======================================

    elif menu == "Withdraw":

        st.header(
            "Withdraw Money"
        )

        st.write(
            f"Available Balance: "
            f"**{Lara_bank_utils.format_currency(account.check_balance())}**"
        )

        amount = st.number_input(
            "Withdrawal Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )


        if st.button(
            "Confirm Withdrawal",
            use_container_width=True
        ):

            if not Lara_bank_utils.is_valid_amount(
                amount
            ):

                st.error(
                    "Invalid withdrawal amount."
                )

            elif amount > account.check_balance():

                st.error(
                    "Insufficient balance."
                )

            else:

                success = account.withdraw(
                    amount
                )

                if success:

                    Lara_bank_storage.update_account(
                        account
                    )

                    Lara_bank_transactions.record_transaction(
                        account,
                        "Withdraw",
                        amount
                    )

                    st.success(
                        "Withdrawal successful."
                    )

                    st.metric(
                        "New Balance",
                        Lara_bank_utils
                        .format_currency(
                            account.check_balance()
                        )
                    )


    # ======================================
    # TRANSACTION HISTORY
    # ======================================

    elif menu == "Transaction History":

        st.header(
            "Transaction History"
        )

        transactions = (
            Lara_bank_transactions
            .get_transactions()
        )


        # Show only transactions
        # belonging to the logged-in user.

        transactions = [
            transaction
            for transaction in transactions
            if transaction.get(
                "account_number"
            ) == account.account_number
        ]


        if transactions:

            display_data = []

            for transaction in transactions:

                display_data.append({

                    "Timestamp":
                        transaction.get(
                            "timestamp",
                            "N/A"
                        ),

                    "Transaction":
                        transaction.get(
                            "transaction",
                            "N/A"
                        ),

                    "Amount":
                        Lara_bank_utils
                        .format_currency(
                            transaction.get(
                                "amount",
                                0
                            )
                        ),

                    "Balance After":
                        Lara_bank_utils
                        .format_currency(
                            transaction.get(
                                "balance_after",
                                0
                            )
                        )
                })


            st.dataframe(
                display_data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No transaction history available."
            )


    # ======================================
    # TRANSACTION ANALYSIS
    # ======================================

    elif menu == "Transaction Analysis":

        st.header(
            "Transaction Analysis"
        )

        result = (
            Lara_bank_analysis
            .analyze_transactions(
                account.account_number
            )
        )


        # ==================================
        # ANALYSIS 1
        # TRANSACTION SUMMARY
        # ==================================

        st.subheader(
            "1. Transaction Summary"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Total Transactions",
            result[
                "total_transactions"
            ]
        )


        col2.metric(
            "Deposits",
            result[
                "deposits"
            ]
        )


        col3.metric(
            "Withdrawals",
            result[
                "withdrawals"
            ]
        )


        st.divider()


        # ==================================
        # ANALYSIS 2
        # MONEY FLOW
        # ==================================

        st.subheader(
            "2. Money Flow Analysis"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Total Deposited",
            Lara_bank_utils
            .format_currency(
                result[
                    "total_deposited"
                ]
            )
        )


        col2.metric(
            "Total Withdrawn",
            Lara_bank_utils
            .format_currency(
                result[
                    "total_withdrawn"
                ]
            )
        )


        col3.metric(
            "Net Cash Flow",
            Lara_bank_utils
            .format_currency(
                result[
                    "net_cash_flow"
                ]
            )
        )


        st.divider()


        # ==================================
        # ANALYSIS 3
        # ACCOUNT ACTIVITY
        # ==================================

        st.subheader(
            "3. Account Activity Analysis"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Largest Transaction",
            Lara_bank_utils
            .format_currency(
                result[
                    "largest_transaction"
                ]
            )
        )


        col2.metric(
            "Average Transaction",
            Lara_bank_utils
            .format_currency(
                result[
                    "average_transaction"
                ]
            )
        )


        col3.metric(
            "Latest Transaction",
            result[
                "latest_transaction"
            ]
        )


        st.caption(
            f"Latest Activity: "
            f"{result['latest_timestamp']}"
        )