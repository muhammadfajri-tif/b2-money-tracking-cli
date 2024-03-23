from os import system, name

class MoneyTrackingUI:
    

    # define our clear function
    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    # UI boder menu
    @staticmethod
    def print_border(width):
        print("╔" + "═" * (width - 2) + "╗")

    @staticmethod
    def print_title(title, width):
        padding = " " * ((width - len(title) - 2) // 2)
        print("║{}{}{}║".format(padding, title, padding + " " * (width % 2)))

    @staticmethod
    def print_menu_option(option, number, width):
        if option == "Exit" or option == "Back":
            number = 0
        padding_number = " " * (2 - len(str(number)))
        padding_option = " " * (width - len(option) - 9)
        print("║ {}{} - {}{} ║".format(number, padding_number, option, padding_option))

    @staticmethod
    def print_border_bottom(width):
        print("╚" + "═" * (width - 2) + "╝")

    @staticmethod
    def print_money_tracking_ui_menu_addMoney():
        title = "Money Tracking"
        menu_options = ["Income", "Spending",]

        width = max(len(title), max(len(option) for option in menu_options)) + 11

        MoneyTrackingUI.print_border(width)
        MoneyTrackingUI.print_title(title, width)
        MoneyTrackingUI.print_border(width)
        for i, option in enumerate(menu_options, start=1):
            MoneyTrackingUI.print_menu_option(option, i, width)
        MoneyTrackingUI.print_border_bottom(width)
        
    @staticmethod
    def print_money_tracking_ui_header():
        title = "Money Tracking App"

        width = len(title) + 11

        MoneyTrackingUI.print_border(width)
        MoneyTrackingUI.print_title(title, width)
        MoneyTrackingUI.print_border_bottom(width) 
        

    @staticmethod
    def print_money_tracking_ui_start_menu():
        title = "Money Tracking App"
        menu_options = ["Add Money","Read All Money", "Export Account", "Import Account", "Exit"]

        width = max(len(title), max(len(option) for option in menu_options)) + 11

        MoneyTrackingUI.print_border(width)
        MoneyTrackingUI.print_title(title, width)
        MoneyTrackingUI.print_border(width)
        for i, option in enumerate(menu_options, start=1):
            MoneyTrackingUI.print_menu_option(option, i, width)
        MoneyTrackingUI.print_border_bottom(width)
        # End UI boder menu