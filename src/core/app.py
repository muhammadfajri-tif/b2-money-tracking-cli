from .account import Account
from storage.user_data import UserData
from .transaction import Transaction, TransactionType


class App:
    # constructor
    def __init__(self):
        if UserData.validate_account_data():
            # validate username, if exist load
            loaded = UserData.import_account_data("account.csv")
            if loaded is not None:
                self.account = Account(loaded["name"], loaded["money"])
                self.account._transactions = loaded["transactions"]
                print("[INFO] Successfully sync data to the file.")
            else:
                print("[ERRO] Failed to load existing data.")
        else:
            account_name = input("Enter account name: ")
            initial_money = input("Enter initial money: ")
            self.account = Account(account_name, int(initial_money))

    def add_money(self):
        date = input("Enter date (YYYY-MM-DD): ")

        print("1. Income")
        print("2. Spending")
        type_input = input("Enter Transaction type: ")

        while(int(type_input) <= 0 or int(type_input) > 2):
            print("[ERRO] Transaction type is not valid.")
            type_input = input("Enter Transaction type: ")

        type = TransactionType.INCOME if int(type_input) == 1 else TransactionType.SPENDING

        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        desc = input("Enter desc: ")

        # if account_name not in self.account:
        #     self.account = Account(account_name)

        transaction = Transaction(type, date, amount, category, desc)
        self.account.add_transaction(transaction)
        print("Money added successfully.")

    def read_all_money(self):
        # account_name = input("Enter account name: ")
        period = input("Enter period (day/week/month/year): ")

        # if account_name in self.accounts:
        transactions = self.account.get_transactions_for_period(period)
        print("Transactions:")
        for transaction in transactions:
            print(
                    f"Type: {transaction.type}, Date: {transaction.date}, Amount: {transaction.amount}, Category: {transaction.category}, Note: {transaction.desc}"
            )
        # else:
        #     print("Account not found.")

    def export_account(self):
        # account_name = input("Enter account name: ")
        filename = input("Enter filename to export: ")

        # if account_name in self.accounts:
        Account.export_account(self.account,filename)
        print("Account exported successfully.")
        # else:
        #     print("Account not found.")

    def import_account(self):
        filename = input("Enter filename to import: ")
        # account_name = input("Enter account name: ")

        loaded = UserData.import_account_data(filename)
        if loaded is not None:
            self.account = Account(loaded["name"], loaded["money"])
            self.account._transactions = loaded["transactions"]
            print("[INFO] Account imported successfully.")
        else:
            print("[ERRO] Failed to load existing data.")
