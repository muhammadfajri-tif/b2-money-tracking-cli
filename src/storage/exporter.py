from core.account import Account


class Exporter:
    @staticmethod
    def export_account(account: Account, filename: str):
        account.export_account(filename)
