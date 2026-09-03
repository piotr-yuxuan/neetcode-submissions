class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name, initial_balance) -> None:
        self.name = name
        self.balance = initial_balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += self.balance


# TODO: Create two accounts
# TODO: Print the information using the mentioned format
a1 = BankAccount("Alice", 1000)
a2 = BankAccount("Bob", 2000)

print(f"Alice's balance: ${a1.balance}")
print(f"Bob's balance: ${a2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")