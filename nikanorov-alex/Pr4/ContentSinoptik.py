from Link import Link
from WeatherFather import WeatherFather
class ContentSinoptik(WeatherFather):
    def __init__(self, html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max):
        super(ContentSinoptik, self).__init__(html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max)

    def outputInf(self, weatherList):
        location_name = Link().enter_the_inf()
        weatherFather = weatherList[0]
        weatherFather2 = weatherList[1]
        weatherFather3 = weatherList[2]

        for i in weatherFather:
            w1 = i
        for i in weatherFather2:
            w2 = i
        for i in weatherFather3:
            w3 = i

        
        print()
        print("------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\t\tПогода з сайту Sinoptik " + location_name)
        print("День:" + w1['title'])
        print("Число: " + w1['date1'], ' ', w1['date2'])
        print("Температура: :" + w1['temp'], " ||  " + w1['temp2'])
        print()

        weather_day = []
        for i in w2:
            weather_day.append(w2[i])

        weather_day2 = []
        for i in w3:
            weather_day2.append(w3[i])

        print("Прогноз на день")
        for i in weather_day:
            print(i, end='     ')
        for j in weather_day2:
            print(j, end='       ')
            if j == weather_day2[4]:
                print(end='  ')
            if j == weather_day2[5]:
                print(end='   ')