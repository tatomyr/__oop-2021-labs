from bs4 import BeautifulSoup
class WeatherFather():
    def __init__(self, html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max):
        self.html = html
        self.mainClass = mainClass
        self.mainNextDay = mainNextDay
        self.tabsContentInner = tabsContentInner
        self.temperature = temperature
        self.pClassOne = pClassOne
        self.pClassTwo = pClassTwo
        self.pClassThree = pClassThree
        self.min = min
        self.max = max
    def start_gettingSinoptik(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        # Ищет в этом классе
        items = soup.find_all('div', class_=self.mainClass)
        weather1 = []
        weather2 = []
        weather3 = []
        weatherNextDay = []
        for item in items:
            weather1.append(dict(
                title=item.find('p', class_= self.pClassOne).get_text(),
                date1=item.find('p', class_= self.pClassTwo).get_text(),
                date2=item.find('p', class_= self.pClassThree).get_text(),
                temp=item.find('div', class_= self.min).get_text(),
                temp2=item.find('div', class_= self.max).get_text(),
            ))
            itemsNextDay = soup.find_all('div', id=self.mainNextDay)
            for item in itemsNextDay:
                weatherNextDay.append(dict(
                    title=item.find('a', class_=self.pClassOne).get_text(),
                    date1=item.find('p', class_=self.pClassTwo).get_text(),
                    date2=item.find('p', class_=self.pClassThree).get_text(),
                    temp=item.find('div', class_=self.min).get_text(),
                    temp2=item.find('div', class_=self.max).get_text(),
                ))

            item2 = soup.find_all('div', class_=self.tabsContentInner)

            for item in item2:
                weather2.append(
                    dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                         vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                         vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                         vol7=item.find('td', class_='p7').get_text(),
                         vol8=item.find('td', class_='p8').get_text()))

            item3 = soup.find_all('tr', class_=self.temperature)

            for item in item3:
                weather3.append(
                    dict(vol1=item.find('td', class_='p1').get_text(), vol2=item.find('td', class_='p2').get_text(),
                         vol3=item.find('td', class_='p3').get_text(), vol4=item.find('td', class_='p4').get_text(),
                         vol5=item.find('td', class_='p5').get_text(), vol6=item.find('td', class_='p6').get_text(),
                         vol7=item.find('td', class_='p7').get_text(),
                         vol8=item.find('td', class_='p8').get_text()))
        return [weather1, weather2, weather3, weatherNextDay]