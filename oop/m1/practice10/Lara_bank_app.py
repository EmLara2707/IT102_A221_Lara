""" 
######### Learning Signature ######### 
Programmed by: Elizabeth Maude M. Lara
Date Submitted: September 6, 2026
 
Program Description: I changed the color and layout of the welcome page and the main page to make it more professional and added a quick actions on the dashboard.
Reflection: I learned how to apply CSS to streamlit.

AI Usage
[/] No AI Assistance - Completed independently without AI.
[ ] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""

import streamlit as st

from datetime import datetime
import Lara_bank_auth
import Lara_bank_storage
import Lara_bank_transactions
import Lara_bank_analysis
import Lara_bank_utils


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Lara Bank | Digital Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# THEME / CUSTOM STYLING
# ==========================================
# A professional banking palette: deep navy for
# trust and stability, a warm gold accent for
# premium touches, and a clean neutral background.

st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

    <style>

        :root {
            --lb-navy-900: #00DEAE;
            --lb-navy-700: #14345C;
            --lb-navy-500: #1F4B7A;
            --lb-gold-500: #00FFF2;
            --lb-gold-600: #1F4B7A;
            --lb-bg: #021426;
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
            color: #FFFFFF;
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
            background-color: var(--lb-bg);
            border: 3px solid black;
            border-right-color: var(--lb-navy-900);
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

        div[data-testid="stTab"][aria-selected="true"] .react-aria-SelectionIndicator {
            background-color: var(--lb-gold-500) !important;
        }

        div[data-testid="stTab"][aria-selected="true"] p {
            color: var(--lb-gold-500) !important;
        }

        label[data-testid="stRadioOption"][data-selected="true"] > div > div > div:first-child {
            background-color: var(--lb-gold-500) !important;
            border-color: var(--lb-gold-500) !important;
        }

        label[data-testid="stRadioOption"][data-selected="true"] > div > div > div:first-child svg {
            fill: var(--lb-gold-500) !important;
            color: var(--lb-gold-500) !important;
        }

        div[data-testid="stTab"]:hover p {
            color: var(--lb-gold-500) !important;
        }

        div[data-testid="stTab"] p {
            color: #EDEFF4;
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

    st.session_state.menu = MENU_OPTIONS[0]

if "pending_menu" in st.session_state:

    st.session_state.menu_radio = st.session_state.pending_menu

    st.session_state.menu = st.session_state.pending_menu

    del st.session_state.pending_menu

# For Pin Lockout, Large Withdrawal OTP, and Custom Transaction Note

if "failed_login_attempts" not in st.session_state:
    st.session_state.failed_login_attempts = 0

if "account_locked" not in st.session_state:
    st.session_state.account_locked = False

if "withdraw_otp" not in st.session_state:
    st.session_state.withdraw_otp = None

if "withdraw_otp_amount" not in st.session_state:
    st.session_state.withdraw_otp_amount = 0.0

if "withdraw_otp_note" not in st.session_state:
    st.session_state.withdraw_otp_note = ""

MAX_LOGIN_ATTEMPTS = 3
OTP_THRESHOLD = 10000.0

# ==========================================
# BANK HEADER / BRANDING
# ==========================================

st.markdown(
    f"""
    <div class="lb-banner">
        <div>
            <p class="lb-banner-title">🏦 Lara Bank</p>
            <p class="lb-banner-sub">Secure Digital Banking System</p>
        </div>
        <div class="lb-banner-badge">🔒 256-bit encrypted session</div>
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# LOGIN / REGISTRATION
# ==========================================

if not st.session_state.logged_in:

    left_space, center, right_space = st.columns(
        [1, 2, 1]
    )

    with center:

        login_tab, register_tab = st.tabs(
            [
                "🔐  Login",
                "📝  Register"
            ]
        )


        # ======================================
        # LOGIN (CHANGED!!!)
        # ======================================

        with login_tab:
            st.subheader("Welcome Back")
            st.caption("Log in with your account number and PIN to continue.")
            st.markdown('<div class="lb-divider-gold"></div>', unsafe_allow_html=True)

            if st.session_state.account_locked:
                st.error("🔒 Too many failed attempts. Login is locked for this session.")
                if st.button("Unlock Login", use_container_width=True):
                    st.session_state.account_locked = False
                    st.session_state.failed_login_attempts = 0
                    st.rerun()
            else:
                account_number = st.text_input("Account Number", key="login_account")
                pin = st.text_input("PIN", type="password", key="login_pin")

                if st.button("Login", use_container_width=True):
                    account, message = Lara_bank_auth.login_account(account_number, pin)

                    if account is not None:
                        st.session_state.logged_in = True
                        st.session_state.account = account
                        st.session_state.failed_login_attempts = 0
                        st.session_state.pending_menu = MENU_OPTIONS[0]
                        st.success(message)
                        st.rerun()
                    else:
                        st.session_state.failed_login_attempts += 1
                        remaining = MAX_LOGIN_ATTEMPTS - st.session_state.failed_login_attempts

                    if remaining <= 0:
                        st.session_state.account_locked = True
                        st.error("🔒 Account locked after 3 failed attempts.")
                    else:
                        st.error(f"{message} ({remaining} attempt(s) remaining)")

            st.markdown("</div>", unsafe_allow_html=True)

        # ======================================
        # REGISTRATION
        # ======================================

        with register_tab:
            st.subheader(
                "Create Your Lara Bank Account"
            )

            st.caption(
                "It takes less than a minute to open an account."
            )

            st.markdown(
                '<div class="lb-divider-gold"></div>',
                unsafe_allow_html=True
            )

            name = st.text_input(
                "Full Name",
                key="register_name"
            )

            account_number = st.text_input(
                "Account Number",
                key="register_account"
            )

            pin_col, confirm_col = st.columns(2)

            with pin_col:

                pin = st.text_input(
                    "Create 4-Digit PIN",
                    type="password",
                    key="register_pin"
                )

            with confirm_col:

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

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


# ==========================================
# LOGGED-IN BANKING APPLICATION
# ==========================================

else:

    account = (
        st.session_state.account
    )

    account_type_label = account.get_account_type()

    balance_display = Lara_bank_utils.format_currency(
        account.check_balance()
    )


    # ======================================
    # SIDEBAR
    # ======================================

    st.sidebar.markdown(
        """
        <p style="font-size:22px; font-weight:800; font-family:'Libre Franklin', sans-serif; margin-bottom:0;">
            🏦 LARA BANK
        </p>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        f"""
        <p class="lb-sidebar-name">{account.account_name}</p>
        <span class="lb-pill">{account_type_label}</span>
        <p style="font-size:12px; color:#9FB0C7; margin-top:6px;">
            Account No. {account.account_number}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        f"""
        <div class="lb-sidebar-balance-card">
            <p class="lb-sidebar-balance-label">AVAILABLE BALANCE</p>
            <p class="lb-sidebar-balance-value">{balance_display}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.divider()

    menu = st.sidebar.radio(
        "BANKING MENU",
        MENU_OPTIONS,
        index=MENU_OPTIONS.index(st.session_state.menu),
        key="menu_radio"
    )

    st.session_state.menu = menu

    st.sidebar.divider()

    if st.sidebar.button(
        "🚪  Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.account = None

        st.session_state.pending_menu = MENU_OPTIONS[0]
        
        st.rerun()


    # ======================================
    # DASHBOARD
    # ======================================

    if menu == MENU_OPTIONS[0]:

        st.header(
            f"Welcome back, {account.account_name.split(' ')[0]} 👋"
        )

        st.caption(
            "Here's a snapshot of your account today."
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Current Balance",
            balance_display
        )

        col2.metric(
            "Account Type",
            account_type_label
        )

        col3.metric(
            "Account Number",
            account.account_number
        )

        st.write("")

        st.subheader("Quick Actions")

        qa1, qa2, qa3, qa4 = st.columns(4)

        with qa1:

            if st.button("💵  Deposit", use_container_width=True):

                st.session_state.pending_menu = MENU_OPTIONS[1]

                st.rerun()

        with qa2:

            if st.button("🏧  Withdraw", use_container_width=True):

                st.session_state.pending_menu = MENU_OPTIONS[2]
                
                st.rerun()

        with qa3:

            if st.button("📜  History", use_container_width=True):

                st.session_state.pending_menu = MENU_OPTIONS[3]
                
                st.rerun()

        with qa4:

            if st.button("📊  Analysis", use_container_width=True):

                st.session_state.pending_menu = MENU_OPTIONS[4]
                
                st.rerun()

        st.divider()

        st.subheader("Recent Activity")

        recent_transactions = [
            transaction
            for transaction in Lara_bank_transactions.get_transactions()
            if transaction.get("account_number") == account.account_number
        ]

        if recent_transactions:

            recent_display = []

            for transaction in recent_transactions[-5:][::-1]:

                recent_display.append({
                    "Timestamp": transaction.get("timestamp", "N/A"),
                    "Transaction": transaction.get("transaction", "N/A"),
                    "Amount": Lara_bank_utils.format_currency(
                        transaction.get("amount", 0)
                    ),
                    "Balance After": Lara_bank_utils.format_currency(
                        transaction.get("balance_after", 0)
                    )
                })

            st.dataframe(
                recent_display,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No recent activity yet. Make your first deposit to get started."
            )


    # ======================================
    # DEPOSIT (CHANGED!!!)
    # ======================================

    elif menu == MENU_OPTIONS[1]:
        st.header("💵 Deposit Money")
        st.markdown('<div class="lb-divider-gold"></div>', unsafe_allow_html=True)
        st.write(f"Current Balance: **{balance_display}**")

        amount = st.number_input("Deposit Amount", min_value=0.0, step=100.0, format="%.2f")
        note = st.text_input("Note (optional)", key="deposit_note")

        if st.button("Confirm Deposit", use_container_width=True):
            if not Lara_bank_utils.is_valid_amount(amount):
                st.error("Invalid deposit amount.")
            else:
                success = account.deposit(amount)
                if success:
                    Lara_bank_storage.update_account(account)
                    Lara_bank_transactions.record_transaction(account, "Deposit", amount, note)
                    st.success("Deposit successful.")
                    st.metric("New Balance", Lara_bank_utils.format_currency(account.check_balance()))

    # ======================================
    # WITHDRAW (CHANGED!!!)
    # ======================================

    elif menu == MENU_OPTIONS[2]:
        st.header("🏧 Withdraw Money")
        st.markdown('<div class="lb-divider-gold"></div>', unsafe_allow_html=True)
        st.write(f"Available Balance: **{balance_display}**")

        amount = st.number_input("Withdrawal Amount", min_value=0.0, step=100.0, format="%.2f")
        note = st.text_input("Note (optional)", key="withdraw_note")

        if st.button("Confirm Withdrawal", use_container_width=True):
            if not Lara_bank_utils.is_valid_amount(amount):
                st.error("Invalid withdrawal amount.")
            elif amount > account.check_balance():
                st.error("Insufficient balance.")
            elif amount >= OTP_THRESHOLD:
                st.session_state.withdraw_otp = Lara_bank_utils.generate_otp()
                st.session_state.withdraw_otp_amount = amount
                st.session_state.withdraw_otp_note = note
                st.info(
                    f"Large withdrawal detected (≥ {Lara_bank_utils.format_currency(OTP_THRESHOLD)}). "
                    f"Your one-time code is **{st.session_state.withdraw_otp}** (simulated SMS)."
                )
            else:
                success = account.withdraw(amount)
                if success:
                    Lara_bank_storage.update_account(account)
                    Lara_bank_transactions.record_transaction(account, "Withdraw", amount, note)
                    st.success("Withdrawal successful.")
                    st.metric("New Balance", Lara_bank_utils.format_currency(account.check_balance()))

        if st.session_state.withdraw_otp:
            st.markdown('<div class="lb-divider-gold"></div>', unsafe_allow_html=True)
            st.write("Enter the one-time code sent to you to confirm this withdrawal.")
            entered_otp = st.text_input("One-Time Code", key="withdraw_otp_input")

            if st.button("Verify & Withdraw", use_container_width=True):
                if entered_otp.strip() == st.session_state.withdraw_otp:
                    success = account.withdraw(st.session_state.withdraw_otp_amount)
                    if success:
                        Lara_bank_storage.update_account(account)
                        Lara_bank_transactions.record_transaction(
                            account,
                            "Withdraw",
                            st.session_state.withdraw_otp_amount,
                            st.session_state.withdraw_otp_note
                        )
                        st.success("Withdrawal successful.")
                        st.metric("New Balance", Lara_bank_utils.format_currency(account.check_balance()))
                    st.session_state.withdraw_otp = None
                    st.session_state.withdraw_otp_amount = 0.0
                    st.session_state.withdraw_otp_note = ""
                else:
                    st.error("Incorrect code. Please try again.")

    # ======================================
    # TRANSACTION HISTORY (CHANGED!!!)
    # ======================================

    elif menu == MENU_OPTIONS[3]:
        st.header("📜 Transaction History")
        st.markdown('<div class="lb-divider-gold"></div>', unsafe_allow_html=True)

        transactions = Lara_bank_transactions.get_transactions()
        transactions = [
            transaction
            for transaction in transactions
            if transaction.get("account_number") == account.account_number
        ]

        st.subheader("Filter")
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            type_filter = st.selectbox("Transaction Type", ["All", "Deposit", "Withdraw"])
        with filter_col2:
            min_amount = st.number_input("Minimum Amount", min_value=0.0, step=100.0, format="%.2f")

        use_date_filter = st.checkbox("Filter by date range")
        start_date = end_date = None
        if use_date_filter:
            date_col1, date_col2 = st.columns(2)
            with date_col1:
                start_date = st.date_input("From")
            with date_col2:
                end_date = st.date_input("To")

        def matches_filters(transaction):
            if type_filter != "All" and transaction.get("transaction") != type_filter:
                return False
            if transaction.get("amount", 0) < min_amount:
                return False
            if start_date or end_date:
                try:
                    ts = datetime.strptime(transaction.get("timestamp", ""), "%Y-%m-%d %H:%M:%S").date()
                except ValueError:
                    return False
                if start_date and ts < start_date:
                    return False
                if end_date and ts > end_date:
                    return False
            return True

        transactions = [t for t in transactions if matches_filters(t)]

        if transactions:
            display_data = []
            for transaction in transactions:
                display_data.append({
                    "Timestamp": transaction.get("timestamp", "N/A"),
                    "Transaction": transaction.get("transaction", "N/A"),
                    "Amount": Lara_bank_utils.format_currency(transaction.get("amount", 0)),
                    "Note": transaction.get("note", "") or "-",
                    "Balance After": Lara_bank_utils.format_currency(transaction.get("balance_after", 0))
                })
            st.dataframe(display_data, use_container_width=True, hide_index=True)
        else:
            st.info("No transactions match your filters.")

    # ======================================
    # TRANSACTION ANALYSIS
    # ======================================

    elif menu == MENU_OPTIONS[4]:

        st.header(
            "📊  Transaction Analysis"
        )

        st.markdown(
            '<div class="lb-divider-gold"></div>',
            unsafe_allow_html=True
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

