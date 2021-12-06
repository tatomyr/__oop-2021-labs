
# SOLID. Рефакторинг коду

## Мета

Освоївши методи SOLID та патерни проектування, переписати код курсового проекту згідно з даними принципами.

## [Посилання на код попереднього проекту](https://github.com/Max-creator11/Kyrsova)

## Зміни

## Bank_app.py

```python
import os
from MenuManagement import MenuManagement
from FileManagement import *
from Switch import Switch


if not os.path.exists("config.dictionary"):
    FileManagement.dump_file()

    FileManagement()
    MenuManagement.static_menu()
    Switch.input_number()
    FileManagement.dump_file()

else:
    FileManagement()
    MenuManagement.static_menu()
    Switch.input_number()
    FileManagement.dump_file()

```

## Switch.py

```python
from MenuManagement import MenuManagement
from Authentification import LoginPass
from BankUser import BankUser


class Switch():
    @staticmethod
    def input_number():
        BankUser.exist = False
        number = input("Type number:")
        if(number == "1"):
            MenuManagement.about_info()
            MenuManagement.static_menu()
            Switch.input_number()

        elif(number == "2"):
            LoginPass()
            LoginPass.check_data()

        elif(number == "3"):
            print("Session is cancelled")
        else:
            print("Error occurred! Try again!")
            MenuManagement.static_menu()
            Switch.input_number()


```

## Authentification.py

```python
from CreateUser import CreateUser
from DeleteUser import DeleteUser
from MenuManagement import MenuManagement
from FileManagement import *
from UserDB import UserDB

class LoginPass():

    def __init__(self):
        LoginPass.login = input("Please, input login:")
        LoginPass.password = input("Please, input password:")

    @classmethod
    def check_data(cls):
        if cls.login == "admin" and cls.password == "admin":
            AdminAuth.check_auth()
        else:
            UserAuth.check_user_auth()


class AdminAuth(LoginPass):
    def check_auth():
        print("Login as an administrator was successful!")
        while True:
            MenuManagement.admin_menu_info()
            state = input()
            if state == "1":
                CreateUser.data_input()
                UserDB.data_to_database()
            elif state == "2":
                DeleteUser.del_user()
            elif state == "3":
                FileManagement.show_info()
            elif state == "4":
                MenuManagement.static_menu()
                break

            else:
                print("Error occurred! Try again!")


class UserAuth(LoginPass):
    def check_user_auth():
        UserDB.change_data_db(LoginPass)
        MenuManagement.static_menu()

```

## User.py

```python
class User():
    def __init__(self, name, second_name, age, gender, login, password):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.gender = gender
        self.login = login
        self.password = password

    def show_details(self):
        print("Personal Details:")
        print("")
        print("Name: ", self.name)
        print("Second Name:", self.second_name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

```

## BankUser.py

```python
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


```

## CreateUser.py

```python
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

```

## DeleteUser.py

```python
from BankUser import BankUser
from FileManagement import *


class DeleteUser(BankUser):

    def del_user():
        FileManagement.show_info()
        try:
            id = int(input("Enter user id: "))
            temp_user = FileManagement.temp_dict_file.pop(id)
            print("User was successfully deleted!")
            del temp_user
        except:
            print("Error occurred! Try again")

```

## UserDB.py

```python
from BankUser import BankUser
from CreateUser import CreateUser
from FileManagement import *
from MenuManagement import MenuManagement


class UserDB(BankUser):
    def data_to_database():
        for obj in FileManagement.temp_dict_file:
            if obj.name == CreateUser.variable.name and obj.password == CreateUser.variable.password and obj.login == CreateUser.variable.login:
                print("Item already exist")
                BankUser.exist = True
        if BankUser.exist == False:
            FileManagement.temp_dict_file.append(CreateUser.variable)

    def change_data_db(cls):
        for obj in FileManagement.temp_dict_file:
            if obj.password == cls.password and obj.login == cls.login:
                print("Login was successful!")
                while True:
                    MenuManagement.user_menu_info()
                    state = input()
                    if state == "1":
                        try:
                            amount = int(input("Enter Deposit amount: "))
                            obj.deposit(amount)
                        except:
                            print("Error occurred! Try again!")

                    elif state == "2":
                        try:
                            amount = int(input("Enter Withdraw amount: "))
                            obj.withdraw(amount)
                        except:
                            print("Error occurred! Try again!")

                    elif state == "3":
                        obj.view_balance()

                    elif state == "4":
                        obj.show_details()

                    elif state == "5":
                        break
                    else:
                        print("Error occurred! Try again!")


```

## FileManagement.py

```python
import pickle


class FileManagement():
    temp_dict_file = []

    def __init__(self):

        with open('config.dictionary', 'rb') as config_dictionary_file:
            FileManagement.config_dictionary = pickle.load(
                config_dictionary_file)
        FileManagement.temp_dict_file = FileManagement.config_dictionary

    @classmethod
    def dump_file(cls):
        with open('config.dictionary', 'wb') as config_dictionary_file:
            pickle.dump(cls.temp_dict_file, config_dictionary_file)

    @classmethod
    def show_info(cls):
        i = 0
        for obj in cls.config_dictionary:
            print(i, ":", obj.name, "-", obj.second_name, "|Gender:",
                  obj.gender, "|Balance:", obj.balance)
            i += 1


```

## MenuManagement.py

```python
class MenuManagement():
    @staticmethod
    def about_info():
        print("___________________________________________________________")
        print("App was created by Maksym Severyn, It-12sp.")
        print("This program shows how a simple banking system works.")
        print("To use it, follow text guide, that appears in the console.")
        print("___________________________________________________________")

    @staticmethod
    def static_menu():
        print("********BANK MANAGEMENT SYSTEM*********")
        print("*----------1:About--------------------*")
        print("*----------2:Login--------------------*")
        print("*----------3:Exit---------------------*")
        print("***************************************")

    @staticmethod
    def user_menu_info():
        print("1:Deposit")
        print("2:Withdraw")
        print("3:View Balance")
        print("4:Show Details")
        print("5:Exit")

    @staticmethod
    def admin_menu_info():
        print("1:Create")
        print("2:Delete")
        print("3:Show users information")
        print("4:Exit")

```

