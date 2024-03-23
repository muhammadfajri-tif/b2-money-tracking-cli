from core.app import App
# from storage.initialization import create_initial_account
from core.UI import MoneyTrackingUI


def main():
    # Create initial account if no account is imported
    app = App()
    # if not app.account:
    #     demo_account = create_initial_account()
    #     app.account = demo_account
    #     print("Initial account created with sample transactions.")

    # Main loop of the application
    while True:
        MoneyTrackingUI.print_money_tracking_ui_start_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            app.add_money()

        elif choice == "2":
            app.read_all_money()

        elif choice == "3":
            app.export_account()

        elif choice == "4":
            app.import_account()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
