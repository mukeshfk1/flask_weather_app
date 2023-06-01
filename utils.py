import requests
import json



def get_weather_data(lat,long,city_name):
    api_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}8&longitude={long}&current_weather=true'

    res = requests.get(api_url)
    data = json.loads(res.text)

    obj = WeatherManager(data,city_name)


    return obj 



class WeatherManager:
    def __init__(self,data,city_name):
        self.lat=data['latitude']
        self.long = data['longitude']
        self.temp = data["current_weather"]['temperature']
        self.wind = data['current_weather']['windspeed']
        self.day = bool(data['current_weather']["is_day"])
        self.city = city_name
        #self.day = False