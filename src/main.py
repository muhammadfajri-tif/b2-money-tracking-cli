from core.app import App
from storage.initialization import create_initial_account


def main():
    # Create initial account if no account is imported
    app = App()
    if not app.accounts:
        demo_account = create_initial_account()
        app.accounts[demo_account.name] = demo_account
        print("Initial account created with sample transactions.")

    # Main loop of the application
    while True:
        print("\nMoney Tracking App")
        print("1. Add Money")
        print("2. Read All Money")
        print("3. Export Account")
        print("4. Import Account")
        print("5. Exit")
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
