from .account import Account
from .transaction import Transaction
from .user_interface import MoneyTrackingUI
import sys
sys.path.append("src/")
from main import main
import time

class App:
    def __init__(self):
        self.accounts = {}


    # fungsi add
    def menu_add_income(self, account_name):
        opt_income = ""
        while True:
            MoneyTrackingUI.clear()
            MoneyTrackingUI.print_money_tracking_ui_menu_add()

            choice = input("Enter your choice: ")

            if choice == '1':
                # modul input date
                date = input("Enter your date (format yyyy-mm-dd): ") 
                if App.valid_date(date):
                    print("Date info:", date)
                else:
                    print("Format date not valid. Make sure your format yyyy-mm-dd.")
                str (date)
                continue
            elif  choice == '2':
                amount = int(input("Enter your amount: Rp."))
                
                continue
            elif choice == '3':
                category: str
                category = App.category_income(opt_income)
                
                continue
            elif choice == '4':
                print("note")
                note = input("Enter your note: ")
            elif choice == '5':
                save = input("Do you want to save? (y/n): ")
                if save == 'y':
                    MoneyTrackingUI.clear()
                    # modul save with parameter date, amount,category, note
                    if save == 'y':
                        MoneyTrackingUI.clear()
                        print(account_name)
                        print(self.accounts)
                    # modul save with parameter date, amount, result, note
                        print ( account_name not in self.accounts)
                        if account_name not in self.accounts:
                            self.accounts[account_name] = Account(account_name)
                        #     self.accounts[account_name] = Account(account_name)

                        transaction = Transaction(date, amount, category)
                        self.accounts[account_name].add_transaction(transaction)
                        print("saved")
                        App.menu_add_plus_income()
                        
                else:
                    continue
            elif choice == '0':
                MoneyTrackingUI.clear()
                return 0
                break
            else:
                print("Invalid choice")

    def menu_add_spending(account_name):
        opt_spending = ""
        while True:
            MoneyTrackingUI.clear()
            MoneyTrackingUI.print_money_tracking_ui_menu_add()

            choice = input("Enter your choice: ")

            if choice == '1':
                # modul input date
                date = input("Enter your date (format yyyy-mm-dd): ") 
                if App.valid_date(date):
                    print("Date info:", date)
                else:
                    print("Format date not valid. Make sure your format yyyy-mm-dd.") 
                continue
            elif choice == '2':
                amount = input("Enter your amount: Rp.")
                int (amount)
                continue
            elif choice == '3':
                category = MoneyTrackingUI.category(opt_spending)
                continue
            elif choice == '4':
                print("note")
                note = input("Enter your note: ")
                continue
            elif choice == '5':
                save = input("Do you want to save? (y/n): ")
                if save == 'y':
                    MoneyTrackingUI.clear()
                    # modul save with parameter date, amount, result, note
                    
                    App.menu_add_plus_spending()
                else:
                    continue
            elif choice == '0':
                MoneyTrackingUI.clear()
                return 0
                break
            else:
                print("Invalid choice")

    # fungsi add plus
    def menu_add_plus_income():
        while True:
            MoneyTrackingUI.clear()
            MoneyTrackingUI.print_money_tracking_ui_menu_add_plus()
            # modul visualisasi rekap income
            choice = input("Enter your choice: ")
            if choice == '1':
                App.menu_add_income()
                continue
            elif choice == '2':
                # modul edit
                print("edit")
                continue
            elif choice == '3':
                # modul delete
                print("delete")
                continue
            elif choice == '0':
                main()
            else:
                print("Invalid choice")

    def menu_add_plus_spending(self):
        while True:
            MoneyTrackingUI.clear()
            MoneyTrackingUI.print_money_tracking_ui_menu_add_plus()
            # modul visualisasi rekap spending
            choice = input("Enter your choice: ")
            if choice == '1':
                self.menu_add_spending()
                continue
            elif choice == '2':
                print("edit")
                continue
            elif choice == '3':
                print("delete")
                continue
            elif choice == '4':
                main()
            else:
                print("Invalid choice")

    # Fungsi category
    def category_income(opt):
        MoneyTrackingUI.clear()
        kategori = ["Grants", "Allowance", "Salary", "Others"]
        while True:
            print("===========================================")
            print("|                Category                 |")
            print("===========================================")
            for i in range(len(kategori)):
                print(f"{i+1}. {kategori[i]}")
            print("===========================================")

            choice = input("Enter your choice: ")

            if choice == '1':
                opt = "Grants"
                return opt
            elif choice == '2':
                opt = "Allowance"
                return opt
            elif choice == '3':
                opt = "Salary"
                return opt
            elif choice == '4':
                opt = "Others"
                return opt
            else:
                print("Invalid choice")


    """ Category for Spending """
    def category_spending(opt_spending):
        MoneyTrackingUI.clear()
        kategori = ["Food/Drink", "Entertainment", "Transportation", "Household", "College", "Medical", "Others"]
        while True:
            print("===========================================")
            print("|                Category                 |")
            print("===========================================")
            for i in range(len(kategori)):
                print(f"{i+1}. {kategori[i]}")
            print("===========================================")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Food/Drink
                opt_spending = "Food/Drink"
                return opt_spending
            elif choice == '2':
                # Entertainment
                opt_spending = "Entertainment"
                return opt_spending
            elif choice == '3':
                # Transportation
                opt_spending = "Transportation"
                return opt_spending
            elif choice == '4':
                # Household
                opt_spending = "Household"
                return opt_spending
            elif choice == '5':
                # College
                opt_spending = "College"
                return opt_spending
            elif choice == '6':
                # Medical
                opt_spending = "Medical"
                return opt_spending
            elif choice == '7':
                # Others
                opt_spending = "Others"
                return opt_spending
            else:
                print("Invalid choice")
    def valid_date(date):
        # Memeriksa panjang string
        if len(date) != 10:
            return False

        # Memeriksa posisi strip ("-")
        if date[4] != "-" or date[7] != "-":
            return False

        # Memeriksa tahun, bulan, dan date apakah numerik
        try:
            tahun, bulan, hari = map(int, date.split("-"))
        except ValueError:
            return False

        # Memeriksa rentang tahun, bulan, dan date
        if tahun < 1000 or tahun > 9999 or bulan < 1 or bulan > 12 or hari < 1 or hari > 31:
            return False

        return True
    
    def read_all_money(self):
        account_name = input("Enter account name: ")
        period = input("Enter period (day/week/month/year): ")

        if account_name in self.accounts:
            transactions = self.accounts[account_name].get_transactions_for_period(
                period
            )
            print("Transactions:")
            for transaction in transactions:
                print(
                    f"Date: {transaction.date}, Amount: {transaction.amount}, Category: {transaction.category}"
                )
        else:
            print("Account not found.")

    def export_account(self):
        account_name = input("Enter account name: ")
        filename = input("Enter filename to export: ")

        if account_name in self.accounts:
            self.accounts[account_name].export_account(filename)
            print("Account exported successfully.")
        else:
            print("Account not found.")

    def import_account(self):
        filename = input("Enter filename to import: ")
        account_name = input("Enter account name: ")

        account = Account.import_account(filename)
        self.accounts[account_name] = account
        print("Account imported successfully.")
