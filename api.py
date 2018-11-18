import requests

class Weather:
    def __init__(self, city, temp):
        self.city = city
        self.temp = temp

    def __str__(self):
        return '''City: %s
Temp: %s''' % (self.city, self.temp)


class WeatherManager:
    KEY = '64331ac3d5fdc2c368d5250b608ed68f'
    URL = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid='+ KEY + '&units=metric'

    def get_weather(self, city, lang='ru'):
        resp = requests.get(self.URL % city)
        data = resp.json()
        return Weather(data['name'], data['main']['temp'])

manager = WeatherManager()
w = manager.get_weather('London', lang='ru')
print(w.city)
print(str(w.temp) + ' C')
