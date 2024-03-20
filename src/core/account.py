import csv
from .transaction import Transaction
from typing import List
from utils.date_utils import parse_date, calculate_date_range


class Account:
    def __init__(self, name: str, total_money: int = 0):
        self.name = name
        self.total_money = total_money
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
        self.total_money += transaction.amount

    def get_transactions_for_period(self, period: str) -> List[Transaction]:
        start_date, end_date = calculate_date_range(period)

        filtered_transactions = []
        for transaction in self.transactions:
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
            for transaction in self.transactions:
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
                date = row["Date"]
                amount = int(row["Amount"])
                category = row["Category"]
                transaction = Transaction(date, amount, category)
                account.add_transaction(transaction)
        return account
