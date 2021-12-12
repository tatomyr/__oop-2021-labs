import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


class pogodikon:
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/88.0.4324.190 Safari/537.36',
        'accept': '*/*'}

    def __init__(self, name):
        self.name = name
        self.q = format(quote("погода-" + self.name))

    def poiskpres_pogoda(self):
        self.url_p = "https://pogoda33.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-" + self.q + "/%D0%B4%D0%B5%D0%BD%D1%8C"
        return self.url_p


class get_html_p(pogodikon):
    def g_html_pogoda(self, url, params=None):
        self.url = url
        self.r_p = requests.get(self.url, headers=self.HEADERS, params=params)
        return self.r_p


class get_content_p:

    def __init__(self):
        self.pog1 = []
        self.pog2 = []
        self.pog3 = []
        self.pog4 = []

    def find_elem(self):
        pass


class get_content_pog(get_content_p):
    def __init__(self, name, n):
        super().__init__()
        self.name_local = n
        self.soup = BeautifulSoup(name, 'html.parser')

        self.items2 = self.soup.find_all('div', class_='days d-none d-lg-block')[0]
        self.into = self.items2.find_all('div', class_='col-md-1 temperature')

        self.items3 = self.soup.find_all('div', class_='current-weather-middle-forecast')[0]
        self.it3 = self.items3.find_all('div', class_='forecast-weather-temperature')

        self.items3 = self.soup.find_all('div', class_='current-weather-middle-forecast')[1]
        self.it4 = self.items3.find_all('div', class_='forecast-weather-temperature')

        self.pog3.append(self.it3[0].text)
        self.pog3.append(self.it4[0].text)

        self.items4 = self.soup.find_all('div', class_='days d-none d-lg-block')[0]
        self.into4 = self.items4.find_all('div', class_='col-md-1 time')

    def find_elem(self):

        for i in range(len(self.into)):
            self.pog2.append(self.into[i].text)

        self.items1 = self.soup.find_all('div', class_='current-weather')
        for item in self.items1:
            self.pog1.append(dict(
                grad=item.find('div', class_='current-weather-temperature').get_text(),
            ))

        for i in self.pog1:
            self.p1 = i

        for i in range(len(self.into4)):
            self.pog4.append(self.into4[i].text)


class show_content_pog(get_content_pog):

    def show(self):

        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Джерело №2")
        print("\t\t\t\t\t\t\t\t\t\tПогода в ", self.name_local)
        print("Температура прямо  зараз: " + self.p1['grad'])
        print("Температура: вдень " + self.pog3[0], "||", "\tввечері " + self.pog3[1])
        print("Прогноз на день")
        for i in self.pog4:
            print(i[:-2] + ":00", end='       ')
        print()
        for i in self.pog2:
            print(i, end='     ')
            if i == self.pog2[4]:
                print(end='  ')
            if i == self.pog2[5]:
                print(end=' ')

        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
