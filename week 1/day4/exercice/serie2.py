#partie1
class BankAccount:
    def __init__(self, username, password):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
        else:
            raise Exception("Authentication failed.")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated.")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Deposit amount must be a positive integer.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated.")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive integer.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
        #partie 2
class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Balance would go below minimum of {self.minimum_balance}.")
        super().withdraw(amount)  
#partie3

class ATM:
    def __init__(self, account_list, try_limit=2):
        # Validate account list
        if not isinstance(account_list, list) or not all(
            isinstance(acc, BankAccount) for acc in account_list
        ):
            raise Exception("account_list must contain instances of BankAccount or its subclasses.")
        
        # Validate try limit
        if not isinstance(try_limit, int) or try_limit <= 0:
            raise Exception("try_limit must be a positive integer. Setting to default value: 2.")
            try_limit = 2
        
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Log In")
            print("2. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                print(f"Login successful! Welcome, {username}.")
                self.show_account_menu(account)
                return
            except Exception as e:
                pass  # Continue checking other accounts

        self.current_tries += 1
        print(f"Invalid login credentials. Attempts left: {self.try_limit - self.current_tries}")

        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Logout")
            choice = input("Select an option: ")

            if choice == "1":
                try:
                    amount = int(input("Enter deposit amount: "))
                    account.deposit(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = int(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                print("Logging out...")
                account.authenticated = False
                break
            else:
                print("Invalid choice. Please try again.")
                              