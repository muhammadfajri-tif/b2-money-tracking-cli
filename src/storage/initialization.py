from core.account import Account
from core.transaction import Transaction


def create_initial_account():
    account = Account("Demo Account")

    # Sample spending transactions
    spending_transactions = [
        Transaction("2024-03-25", 5000, "Groceries", "medicine"),
        Transaction("2024-03-20", 20000, "Dining Out", "nice food and coke"),
        Transaction("2024-03-25", 3000, "Transportation"),
        Transaction("2024-03-20", 40000, "Entertainment", "cinema"),
        Transaction("2024-03-25", 25000, "Utilities", "household"),
    ]

    # Sample income transactions
    income_transactions = [
        Transaction("2024-03-23", 1_000_000, "Salary"),
        Transaction("2024-03-22", 200_000, "Freelancing", "jobstreet"),
        Transaction("2024-03-28", 100_000, "Bonus", "bonus from work"),
        Transaction("2024-03-22", 40_000, "Investment", "stock liquidity"),
        Transaction("2024-03-28", 5000, "Gift", "cashback"),
    ]

    # Add transactions to the account
    for transaction in spending_transactions + income_transactions:
        account.add_transaction(transaction)

    return account
