from Request import Request
from Link import Link
from ContentSinoptik import ContentSinoptik
from WeatherFather import WeatherFather
# Вивід информації х sinoptik
sinoptikLink = Link().search_per_sinoptik("погода-"+Link().enter_the_inf())
sinoptikRequest = Request(sinoptikLink)
sinoptikResponse = sinoptikRequest.get_html()
sinoptikOutputInf = ContentSinoptik(sinoptikResponse, 'main loaded', "bd2", 'tabsContentInner', 'temperature', 'day-link', 'date', 'month', 'min', 'max')
sinoptikOutputInf.outputInf(sinoptikOutputInf.start_gettingSinoptik())