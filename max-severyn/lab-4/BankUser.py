
class BankUser():
    def __init__(self, name, second_name, age, gender, login, password):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.gender = gender
        self.login = login
        self.password = password
        self.balance = 0
        BankUser.exist = False

    def show_details(self):
        print("Personal Details:")
        print("")
        print("Name: ", self.name)
        print("Second Name:", self.second_name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

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
