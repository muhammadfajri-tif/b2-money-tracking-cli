import csv
from .transaction import Transaction, TransactionType
from typing import List
from utils.date_utils import parse_date, calculate_date_range

class Account:
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

    def update_transaction(self, idx_transaction: int, new_transaction: Transaction) -> Transaction:
        """Method for update/replace exisiting transaction using its index with new transaction"""
        exist_transaction = self._transactions[idx_transaction]
        self._transactions = list(map(lambda transaction: new_transaction if transaction == exist_transaction else transaction, self._transactions))
        return new_transaction

    def delete_transaction(self, idx_transaction: int) -> Transaction:
        """Method for delete existing transaction using its index"""
        deleted_transaction = self._transactions[idx_transaction]
        self._transactions.remove(deleted_transaction)
        return deleted_transaction

    def get_transactions_for_period(self, period: str) -> List[Transaction]:
        start_date, end_date = calculate_date_range(period)
        filtered_transactions = []
        for transaction in self._transactions:
            transaction_date = parse_date(transaction.date)
            if start_date <= transaction_date <= end_date:
                filtered_transactions.append(transaction)
        return filtered_transactions

    def get_income_list(self) -> List[Transaction]:
        """Method for get income list"""
        return list(filter(lambda transaction: transaction.type == TransactionType.INCOME, self._transactions))

    def get_spending_list(self) -> List[Transaction]:
        """Method for get spending list"""
        return list(filter(lambda transaction: transaction.type == TransactionType.SPENDING, self._transactions))

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
