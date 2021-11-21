from User import User


class BankUser(User):
    def __init__(self, name, second_name, age, gender, login, password):
        super().__init__(name, second_name, age, gender, login, password)
        BankUser.exist = False
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance+self.amount
        print("Account balance has beeen updated: ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(
                "Error! Given number is bigger then your balance! Balance Available:", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: ", self.balance)

    def view_balance(self):
        print("Account balance: ", self.balance)
