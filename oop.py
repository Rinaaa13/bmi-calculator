class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        print("Account Information for {} {}:".format(self.firstname, self.lastname))
        print("Total Income: {}".format(self.total_income()))
        print("Total Expenses: {}".format(self.total_expense()))
        print("Account Balance: {}".format(self.account_balance()))

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def account_balance(self):
        return self.total_income() - self.total_expense()

account = PersonAccount("Aurora", "Luna")
account.add_income("Salary", 5000)
account.add_income("Freelancing", 1500)
account.add_expense("Rent", 1200)
account.add_expense("Groceries", 500)
account.add_expense("Utilities", 300)

account.account_info()

print("\nDetails of income and expenses:")
print("Incomes:", account.incomes)
print("Expenses:", account.expenses)
print("Total Income:", account.total_income())
print("Total Expense:", account.total_expense())
print("Account Balance:", account.account_balance())