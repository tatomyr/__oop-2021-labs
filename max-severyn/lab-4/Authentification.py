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
