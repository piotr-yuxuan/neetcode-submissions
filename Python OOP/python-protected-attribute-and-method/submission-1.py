class Account:
    def __init__(self, title, initial_balance):
        self.title = title
        self._balance = initial_balance
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
