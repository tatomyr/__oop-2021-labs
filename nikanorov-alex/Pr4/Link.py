from urllib.parse import quote
class Link:
    def __init__(self):
        pass

    def enter_the_inf(self):
        print("Потрібно ввести назву міста спочатку на російській потім на англійській, нажміть на enter ще раз після першого вводу")
        acq_information = str(input(("Введіть назву міста:")))
        return acq_information
    def search_per_sinoptik(self, nameLocation):
        sinoptik_url = "https://ua.sinoptik.ua/{0}".format(quote(nameLocation))
        return sinoptik_url

