import csv
import os
from .transaction import Transaction, TransactionType
from typing import List
from storage.user_data import UserData
from utils.date_utils import parse_date, calculate_date_range

class Account:
    # private field
    _name: str
    _total_money: int = 0
    _transactions: List[Transaction] = []

    def __init__(self, name: str, total_money: int = 0):
        # # TOOO: validate username, if exist load, if not create new
        # if UserData.validate_account_data():
        #     # if username is same with account file, then sync data transaction
        #     if self._name == name:
        #         loaded = self.import_account("account.csv")
        #         self._name = loaded._name
        #         self._total_money = loaded._total_money
        #         # sort by date
        #         self._transactions = sorted(loaded._transactions, key=lambda trx: trx.date)
        #         print("[INFO] Successfully sync data to the file.")
        #     else:
        #         # overwrite it?
        #         print("[ERRO] Data from file not match with existing account")
        # else: 
        # creating new account
        self._name = name
        self._total_money = total_money
        # create file
        UserData.create_account_data(self._name, self._total_money)

    def get_income_list(self) -> List[Transaction]:
        """Method for get income list"""
        income_transactions = list(filter(lambda transaction: transaction.type == TransactionType.INCOME, self._transactions))
        return sorted(income_transactions, key=lambda trx: trx.date)

    def get_spending_list(self) -> List[Transaction]:
        """Method for get spending list"""
        spending_transactions = list(filter(lambda transaction: transaction.type == TransactionType.SPENDING, self._transactions))
        return sorted(spending_transactions, key=lambda trx: trx.date)

    def get_transactions_list(self) -> List[Transaction]:
        """Method fot get all transactions; transactions sorted by date"""
        return sorted(self._transactions, key=lambda trx: trx.date)

    def get_transactions_for_period(self, period: str) -> List[Transaction]:
        start_date, end_date = calculate_date_range(period)
        filtered_transactions = []
        for transaction in self._transactions:
            transaction_date = parse_date(transaction.date)
            if start_date <= transaction_date <= end_date:
                filtered_transactions.append(transaction)
        return filtered_transactions


    def add_transaction(self, transaction: Transaction):
        """Method to add new transaction"""

        # add new transaction to the list
        self._transactions.append(transaction)
        # mutate field money
        if transaction.type == "income":
            self._total_money += transaction.amount
        elif transaction.type == "spending":
            self._total_money -= transaction.amount
        #sort by date
        self._transactions = sorted(self._transactions, key=lambda trx: trx.date)
        # append to the file
        UserData.add_transaction_to_account(transaction)


    def update_transaction(self, idx_transaction: int, new_transaction: Transaction) -> Transaction:
        """Method for update/replace exisiting transaction using its index with new transaction"""

        # get data by index
        exist_transaction = self._transactions[idx_transaction]
        # update if existing transaction found
        self._transactions = list(map(lambda transaction: new_transaction if transaction == exist_transaction else transaction, self._transactions))
        # update data to the file
        UserData.mutate_transactions_data(self._name, self._total_money, self._transactions)
        return new_transaction


    def delete_transaction(self, idx_transaction: int) -> Transaction:
        """Method for delete existing transaction using its index"""
        # get data by index
        deleted_transaction = self._transactions[idx_transaction]
        try:
            # delete existing record if found
            self._transactions.remove(deleted_transaction)
            # update data to the file
            UserData.mutate_transactions_data(self._name, self._total_money, self._transactions)
        except Exception:
            print("[ERRO] Failed to delete transaction. Index out of range or data not found!")
        return deleted_transaction


    # def export_account(self, filename: str):
    #     if not filename.endswith(".csv"):
    #         filename += ".csv"

    #     with open(filename, "w", newline="") as csvfile:
    #         fieldnames = ["Date", "Amount", "Category"]
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writeheader()
    #         for transaction in self._transactions:
    #             writer.writerow(
    #                 {
    #                     "Date": transaction.date,
    #                     "Amount": transaction.amount,
    #                     "Category": transaction.category,
    #                 }
    #             )


    @staticmethod
    def import_account(filename: str) -> "Account":
        """Method for import/load account data from file"""
        account = Account("")
        dir = os.getcwd()
        file_path = os.path.join(dir, 'data', filename)
        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for idx, row in enumerate(reader):
                    if idx == 0:
                        account._name = row["name"]
                        account._total_money = int(row["money"])
                    if idx > 1:
                        type = row["type"]
                        date = row["date"]
                        amount = int(row["amount"])
                        category = row["category"]
                        desc = row["desc"]
                        transaction = Transaction(TransactionType[type],date, amount, category, desc)
                        account.add_transaction(transaction)
        except IOError:
            print("[ERRO] Failed to import data.")
        return account


    @staticmethod
    def export_account(account: "Account", filename: str = "backup_account.csv"):
        """Method for export account data to file"""
        dir = os.getcwd()
        file_path = os.path.join(dir, 'data', filename)
        try:
            with open(file_path, 'w') as file:
                # create csv dict writer object
                writer = csv.DictWriter(file, fieldnames=UserData._header_field)
                # writing headers / field name
                writer.writeheader()
                # writing account information
                writer.writerow({
                    "name": account._name,
                    "money": account._total_money
                })
                # iterate each transactions
                for transaction in account._transactions:
                    # writing data row
                    writer.writerow({
                        "type": str(transaction.type),
                        "date": transaction.date,
                        "amount": transaction.amount,
                        "category": transaction.category,
                        "desc": transaction.desc
                    })
        except IOError:
            print("[ERRO] Failed to backup account data.")
