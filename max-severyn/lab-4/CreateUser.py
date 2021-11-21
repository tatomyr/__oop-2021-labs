from BankUser import BankUser


class CreateUser(BankUser):
    variable = None

    @classmethod
    def data_input(cls):
        name = input("Name: ")
        second_name = input("Second Name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        login = input("Enter login: ")
        password = input("Enter password: ")
        cls.variable = input("Id: ")
        cls.variable = BankUser(name, second_name, age,
                                gender, login, password)
