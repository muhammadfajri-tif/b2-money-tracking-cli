import os
import csv
from core.transaction import Transaction, TransactionType


class UserData:
    # private field
    _account_file_name = "account.csv"
    _header_field = ['name', 'money', 'type', 'date', 'amount', 'category', 'desc'] 

    @staticmethod
    def get_file_path() -> str:
        """Method for get path to file that handle account data"""
        dir = os.getcwd()
        return os.path.join(dir, 'data', UserData._account_file_name)

    @staticmethod
    def account_data_is_exist() -> bool:
        """Method for check if file that handle account data is exist or not"""
        file_path = UserData.get_file_path()
        return os.path.isfile(file_path) and os.path.getsize(file_path) > 0

    @staticmethod
    def validate_account_data() -> bool:
        """Method for validate file that handle account data has valid data or not"""
        file_path = UserData.get_file_path()
        if UserData.account_data_is_exist():
            try:
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    # get header account.csv as array
                    header = next(reader)
                    # compare with existing header
                    return UserData._header_field == header
            except IOError:
                return False
        # default is false
        return False

    @staticmethod
    def create_account_data(name: str, money: int):
        """Method for create file for new account"""
        file_path = UserData.get_file_path()
        try:
            with open(file_path, 'w') as file:
                # writer = csv.writer(file)
                writer = csv.DictWriter(file, fieldnames=UserData._header_field)
                # create header
                writer.writeheader()
                # writer.writerow(UserData._header_field)
                #create body, contains account information
                writer.writerow({
                    "name": name,
                    "money": money
                })
                # account_field = [name, money, "income", str(date.today()), 0, "", ""]
                # writer.writerow(account_field)
                print("[INFO] Success create account data")
        except IOError:
            print("[ERRO] Failed to create file " + file_path)

    @staticmethod
    def add_transaction_to_account(transaction: Transaction):
        """Method for append new data to the file"""
        file_path = UserData.get_file_path()
        try:
            # append to new file
            with open(file_path, 'a') as file:
                # create csv dict writer object
                writer = csv.DictWriter(file, fieldnames=UserData._header_field)
                # writing data row
                writer.writerow({
                    "type": str(transaction.type),
                    "date": transaction.date,
                    "amount": transaction.amount,
                    "category": transaction.category,
                    "desc": transaction.desc
                })
        except IOError:
                print(f"[ERRO] Failed to add new data: {transaction.type}, {transaction.date}, {transaction.amount}, {transaction.category}")

    @staticmethod
    def mutate_transactions_data(name: str, money: int, transactions: list[Transaction]):
        """Method for mutate transaction data and add to the file. Can be used for update/delete transaction"""
        # handle file path when param filename is filled
        file_path = UserData.get_file_path()

        try:
            with open(file_path, 'w+') as file:
                # create csv dict writer object
                writer = csv.DictWriter(file, fieldnames=UserData._header_field)
                # writing headers / field name
                writer.writeheader()
                # writing account information
                writer.writerow({
                    "name": name,
                    "money": money
                })
                # iterate each transactions
                for transaction in transactions:
                    # writing data row
                    writer.writerow({
                        "type": str(transaction.type),
                        "date": transaction.date,
                        "amount": transaction.amount,
                        "category": transaction.category,
                        "desc": transaction.desc
                    })
        except IOError:
            print("[ERRO] Failed to update transactions to file.")


    @staticmethod
    def import_account_data(filename: str):
        """Method for import/load account data from file"""
        # if user didn't include extension
        if not filename.endswith(".csv"):
            filename += ".csv"

        dir = os.getcwd()
        file_path = os.path.join(dir, 'data', filename)
        try:
            with open(file_path, 'r') as csvfile:
                # default field
                name = ""
                total_money = 0
                transactions: list[Transaction] = []
                # read csv
                reader = csv.DictReader(csvfile)
                # iterate and assign
                for idx, row in enumerate(reader):
                    # get name and initial money
                    if idx == 0:
                        name = row["name"]
                        total_money = row["money"]
                    # get transactions data
                    if idx > 0:
                        type = row["type"]
                        date = row["date"]
                        amount = int(row["amount"])
                        category = row["category"]
                        desc = row["desc"]
                        transaction = Transaction(TransactionType[str(type).upper()],date, amount, category, desc)
                        transactions.append(transaction)
                csvfile.close()

            return {"name": name, "money": total_money, "transactions": transactions}
        except IOError:
            print("[ERRO] Failed to import data.")
