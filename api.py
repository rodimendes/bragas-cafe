import requests

api_code = "f67860a476fc4b2218fcf7932b929ff6" #COLOCAR COMO VARIÁVEL DE AMBIENTE
parameters = {
    "appid": api_code,
    "units": "metric",
    "lat": 41.545448,
    "lon": -8.426507,
    "exclude": "minutely,hourly,daily,alerts"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status
weather_data = response.json()
print(weather_data)
