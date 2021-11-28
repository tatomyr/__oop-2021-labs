from BankUser import BankUser
from MenuManagement import MenuManagement
from FileManagement import *
from UserDB import UserDB
from User import User


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
                User.create_user()
                UserDB.data_to_database()
            elif state == "2":
                User.del_user()
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
