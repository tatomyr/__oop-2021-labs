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
