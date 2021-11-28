from BankUser import BankUser
from FileManagement import FileManagement


class User(BankUser):
    variable = None

    @classmethod
    def create_user(cls):
        name = input("Name: ")
        second_name = input("Second Name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        login = input("Enter login: ")
        password = input("Enter password: ")
        cls.variable = input("Id: ")
        cls.variable = BankUser(name, second_name, age,
                                gender, login, password)

    def del_user():
        FileManagement.show_info()
        try:
            id = int(input("Enter user id: "))
            temp_user = FileManagement.temp_dict_file.pop(id)
            print("User was successfully deleted!")
            del temp_user
        except:
            print("Error occurred! Try again")
