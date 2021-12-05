from BankAccount import BankAccount
from FileManagement import *
from MenuManagement import MenuManagement
from AccountOperations import AccountOperations


class UserDB(BankAccount):
    def data_to_database():
        for obj in FileManagement.temp_dict_file:
            if obj.name == AccountOperations.variable.name and obj.password == AccountOperations.variable.password and obj.login == AccountOperations.variable.login:
                print("Item already exist")
                BankAccount.exist = True
        if BankAccount.exist == False:
            FileManagement.temp_dict_file.append(AccountOperations.variable)

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
