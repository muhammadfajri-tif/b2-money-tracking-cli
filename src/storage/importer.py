from core.account import Account


class Importer:
    @staticmethod
    def import_account(filename: str) -> Account:
        return Account.import_account(filename)
