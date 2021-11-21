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

   
