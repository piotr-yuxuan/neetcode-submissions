class BankAccount:
    def __init__(self, balance: int):
        self.__balance:int = balance
    
    # TODO: Add getter method for balance
    def get_balance(self) -> int:
        return self.__balance

    # TODO: Add setter method for balance
    def set_balance(self, new_balance) -> None:
        if 0 <= new_balance:
            self.__balance = new_balance
        else:
            print("Cannot set negative balance!")



# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
