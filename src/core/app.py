from .account import Account
from .transaction import Transaction, TransactionType


class App:
    def __init__(self):
        self.accounts = {}

    def add_money(self):
        account_name = input("Enter account name: ")
        date = input("Enter date (YYYY-MM-DD): ")

        print("1. Income")
        print("2. Spending")
        type_input = int(input("Enter Transaction type: "))

        while (type_input != 1) and (type_input != 2):
            print("[ERRO] Transaction type is not valid.")
            type_input = input("Enter Transaction type: ")
            if not type_input.isalpha():
                type_input = int(type_input)
            else:
                type_input = 0

        type = TransactionType.INCOME if type_input == 1 else TransactionType.SPENDING

        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        desc = input("Enter desc: ")

        if account_name not in self.accounts:
            self.accounts[account_name] = Account(account_name)

        transaction = Transaction(type, date, amount, category, desc)
        self.accounts[account_name].add_transaction(transaction)
        print("Money added successfully.")

    def read_all_money(self):
        account_name = input("Enter account name: ")
        period = input("Enter period (day/week/month/year): ")

        if account_name in self.accounts:
            transactions = self.accounts[account_name].get_transactions_for_period(
                period
            )
            print("Transactions:")
            for transaction in transactions:
                print(
                    f"Date: {transaction.date}, Amount: {transaction.amount}, Category: {transaction.category}"
                )
        else:
            print("Account not found.")

    def export_account(self):
        account_name = input("Enter account name: ")
        filename = input("Enter filename to export: ")

        if account_name in self.accounts:
            self.accounts[account_name].export_account(filename)
            print("Account exported successfully.")
        else:
            print("Account not found.")

    def import_account(self):
        filename = input("Enter filename to import: ")
        account_name = input("Enter account name: ")

        account = Account.import_account(filename)
        self.accounts[account_name] = account
        print("Account imported successfully.")
