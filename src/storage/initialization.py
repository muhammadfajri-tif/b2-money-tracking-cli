from core.account import Account
from core.transaction import Transaction


def create_initial_account():
    account = Account("Demo Account")

    # Sample spending transactions
    spending_transactions = [
        Transaction("2024-03-25", 50.0, "Groceries"),
        Transaction("2024-03-20", 20.0, "Dining Out"),
        Transaction("2024-03-25", 30.0, "Transportation"),
        Transaction("2024-03-20", 40.0, "Entertainment"),
        Transaction("2024-03-25", 25.0, "Utilities"),
    ]

    # Sample income transactions
    income_transactions = [
        Transaction("2024-03-23", 1000.0, "Salary"),
        Transaction("2024-03-22", 200.0, "Freelancing"),
        Transaction("2024-03-28", 300.0, "Bonus"),
        Transaction("2024-03-22", 400.0, "Investment"),
        Transaction("2024-03-28", 500.0, "Gift"),
    ]

    # Add transactions to the account
    for transaction in spending_transactions + income_transactions:
        account.add_transaction(transaction)

    return account
