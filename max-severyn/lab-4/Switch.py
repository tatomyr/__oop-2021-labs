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
