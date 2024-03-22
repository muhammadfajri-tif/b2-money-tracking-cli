import csv
from .transaction import Transaction, TransactionType
from typing import List
from storage.user_data import UserData
from utils.date_utils import parse_date, calculate_date_range

class Account(UserData):
    # private field
    _transactions: List[Transaction] = []
    _total_money: int = 0

    def __init__(self, name: str, total_money: int = 0):
        # TOOO: validate username, if exist load, if not create new
        self.name = name
        self._total_money = total_money

    def add_transaction(self, transaction: Transaction):
        """Method to add new transaction"""
        # add new transaction to the list
        self._transactions.append(transaction)
        # mutate field money
        if transaction.type == "income":
            self._total_money += transaction.amount
        elif transaction.type == "spending":
            self._total_money -= transaction.amount
        # append to the file

    def get_transactions_for_period(self, period: str) -> List[Transaction]:
        start_date, end_date = calculate_date_range(period)
        filtered_transactions = []
        for transaction in self._transactions:
            transaction_date = parse_date(transaction.date)
            if start_date <= transaction_date <= end_date:
                filtered_transactions.append(transaction)

        return filtered_transactions

    def export_account(self, filename: str):
        if not filename.endswith(".csv"):
            filename += ".csv"

        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Date", "Amount", "Category"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in self._transactions:
                writer.writerow(
                    {
                        "Date": transaction.date,
                        "Amount": transaction.amount,
                        "Category": transaction.category,
                    }
                )

    @classmethod
    def import_account(cls, filename: str) -> "Account":
        account = cls("")
        with open(filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                type = row["type"]
                date = row["date"]
                amount = int(row["amount"])
                category = row["category"]
                desc = row["desc"]
                transaction = Transaction(TransactionType[type],date, amount, category, desc)
                account.add_transaction(transaction)
        return account
