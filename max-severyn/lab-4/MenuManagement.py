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
