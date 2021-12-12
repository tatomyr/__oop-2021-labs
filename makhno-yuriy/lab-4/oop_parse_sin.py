from oop_parse_pog import *


class sinoptikon:
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/88.0.4324.190 Safari/537.36',
        'accept': '*/*'}

    def __init__(self, name):
        self.name = name
        self.q = format(quote("погода-" + self.name))

    def poiskpres_sinoptik(self):
        self.url_s = "https://ua.sinoptik.ua/{0}".format(self.q)
        return self.url_s


class get_html_s(sinoptikon):

    def g_html_sinoptik(self, url, params=None):
        self.url = url
        self.r_s = requests.get(self.url, headers=self.HEADERS, params=params)
        return self.r_s


class get_content_s:

    def __init__(self):
        # sin
        self.weather1 = []
        self.weather2 = []
        self.weather3 = []

    def find_elem(self):
        pass


class get_content_sin(get_content_s):

    def __init__(self, name, n):
        super().__init__()
        self.name_local = n
        self.html = name
        self.soup = BeautifulSoup(self.html, 'html.parser')

        self.item1 = self.soup.find_all('div', class_='main loaded')
        self.item2 = self.soup.find_all('div', class_='tabsContentInner')
        self.item3 = self.soup.find_all('tr', class_='temperature')

    def find_elem(self):
        for i in self.item1:
            self.weather1.append(dict(
                title=i.find('p', class_='day-link').get_text(),
                date1=i.find('p', class_='date').get_text(),
                date2=i.find('p', class_='month').get_text(),
                temp=i.find('div', class_='min').get_text(),
                temp2=i.find('div', class_='max').get_text()))

        for item in self.item2:
            self.weather2.append(
                dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                     vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                     vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                     vol7=item.find('td', class_='p7').get_text(),
                     vol8=item.find('td', class_='p8').get_text()))

        for item in self.item3:
            self.weather3.append(
                dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                     vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                     vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                     vol7=item.find('td', class_='p7').get_text(),
                     vol8=item.find('td', class_='p8').get_text()))

        for i in self.weather1:
            self.w1 = i
        for i in self.weather2:
            self.w2 = i
        for i in self.weather3:
            self.w3 = i


class show_content_sin(get_content_sin):

    def show(self):

        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("Джерело №1")
        print("\t\t\t\t\t\t\t\t\t\tПогода в ", self.name_local)
        print("День:" + self.w1['title'])
        print("Число: " + self.w1['date1'], ' ', self.w1['date2'])
        print("Температура: :" + self.w1['temp'], " ||  " + self.w1['temp2'])
        print()

        self.mw3 = []
        self.mw2 = []

        for i in self.w2:
            self.mw2.append(self.w2[i])
        for i in self.w3:
            self.mw3.append(self.w3[i])
        print("Прогноз на день")
        for i in self.mw2:
            print(i, end='     ')
        print()
        for j in self.mw3:
            print(j, end='       ')
            if j == self.mw3[4]:
                print(end='  ')
            if j == self.mw3[5]:
                print(end='  ')

        print()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
