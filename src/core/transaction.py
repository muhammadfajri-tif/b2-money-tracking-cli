from enum import StrEnum

class TransactionType(StrEnum):
    INCOME = "income"
    SPENDING = "spending"

class Transaction:
    def __init__(self, type: TransactionType, date: str, amount: int, category: str, desc: str = ''):
        self.type = type
        self.date = date
        self.amount = amount
        self.category = category
        self.desc = desc

    @staticmethod
    def validate_transaction_type(type: TransactionType) -> bool:
        """Method for validate transaction type from user input"""
        return type in TransactionType

    def __repr__(self) -> str:
        """To String method"""
        tostr = "{\n"
        tostr += f"\tType: {self.type}\n"
        tostr += f"\tDate: {self.date}\n"
        tostr += f"\tAmount: {self.amount}\n"
        tostr += f"\tCategory: {self.category}\n"
        tostr += f"\tDesc: {self.desc}\n"
        tostr += "}\n"
        return tostr
