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
