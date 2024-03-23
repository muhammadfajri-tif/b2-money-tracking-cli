from storage.initialization import create_initial_account
from core.user_interface import MoneyTrackingUI

def main():
    # account_name = input("Enter account name: ")
    while True:
        # Create initial account if no account is imported
        from core.app import App
        app = App()
        if not app.accounts:
            demo_account = create_initial_account()
            app.accounts[demo_account.name] = demo_account
            print("Initial account created with sample transactions.")

        account_name = input("Enter account name: ")
    
        MoneyTrackingUI.print_money_tracking_ui_start_menu()

        # Mendapatkan input dari pengguna

        selected_option = input("Enter adayour choice: ")

        # Melakukan sesuatu berdasarkan opsi yang dipilih
        if selected_option.isdigit():
            selected_option = int(selected_option)
        if selected_option == 1:
            app.menu_add_income(account_name)
        elif selected_option == 2:
            app.menu_add_spending(account_name)
        elif selected_option == 3:
            app.read_all_money()
        elif selected_option == 4:
            app.export_account()
        elif selected_option == 5:
            app.import_account()
        elif selected_option == 0:
            return 0
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
    

