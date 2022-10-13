import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_CODE = os.environ.get("OWM_API_KEY")

def weather_checker(latitude=41.545448, longitude=-8.426507):
    parameters = {
        "appid": API_CODE,
        "units": "metric",
        "lat": latitude,
        "lon": longitude,
        "exclude": "minutely,hourly,daily,alerts"
    }
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    response.raise_for_status
    weather_data = response.json()
    current_weather = weather_data['current']['weather'][0]['id']
    return current_weather


def city_lat_long(city):
    parameters = {
        "appid": API_CODE,
        "q": city,
        "limit": 1
    }
    response = requests.get(url="http://api.openweathermap.org/geo/1.0/direct", params=parameters)
    response.raise_for_status
    city_data = response.json()
    lat = city_data[0]['lat']
    long = city_data[0]['lon']
    return lat, long
