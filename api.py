import requests

API_CODE = "f67860a476fc4b2218fcf7932b929ff6" #COLOCAR COMO VARIÁVEL DE AMBIENTE

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
    current_weather_icon = weather_data['current']['weather'][0]['icon']
    return current_weather, current_weather_icon
