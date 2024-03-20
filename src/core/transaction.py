class Transaction:
    def __init__(self, date: str, amount: int, category: str, desc: str = ''):
        self.date = date
        self.amount = amount
        self.category = category
        self.desc = desc

