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
            weatherToday = i
        for i in weatherFather2:
            weatherDayTime= i
        for i in weatherFather3:
            weatherDayNumbers = i

        
        print()
        print("------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\t\tПогода з сайту Sinoptik " + location_name)
        print("День:" + weatherToday['title'])
        print("Число: " + weatherToday['date1'], ' ', weatherToday['date2'])
        print("Температура: " + weatherToday['temp'], " ||  " + weatherToday['temp2'])
        print()

        weather_day_output = []
        for i in weatherDayTime:
            weather_day_output.append(weatherDayTime[i])

        weather_day_output2 = []
        for i in weatherDayNumbers:
            weather_day_output2.append(weatherDayNumbers[i])

        print("Прогноз на день")
        for i in weather_day_output:
            print(i, end='     ')
        for j in weather_day_output2:
            print(j, end='       ')
            if j == weather_day_output2[4]:
                print(end='  ')
            if j == weather_day_output[5]:
                print(end='   ')