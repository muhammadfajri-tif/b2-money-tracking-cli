from core.app import App


def main():
    app = App()

    # Main loop of the application
    while True:
        print("\nMoney Tracking App")
        print("1. Add Money")
        print("2. Read All Money")
        print("3. Export Money")
        print("4. Export Account")
        print("5. Import Account")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            app.add_money()

        elif choice == "2":
            app.read_all_money()

        elif choice == "3":
            app.export_money_by_period()

        elif choice == "4":
            app.export_account()

        elif choice == "5":
            app.import_account()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
