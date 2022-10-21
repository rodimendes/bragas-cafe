import requests
import os
from dotenv import load_dotenv
import smtplib


load_dotenv()
API_CODE = os.environ.get("OWM_API_KEY")
DEPARTURE_MAIL = os.environ.get("DEPARTURE_MAIL")
PASS_DEPART_MAIL = os.environ.get("PASS_DEPART_MAIL")
ARRIVAL_MAIL = os.environ.get("ARRIVAL_MAIL")


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
    city_name = city_data[0]['name']
    city_country = city_data[0]['country']
    lat = city_data[0]['lat']
    long = city_data[0]['lon']
    return lat, long, city_name, city_country

def send_email(name, address, email):
    email_message = f"Subject:New café to visit!! 🥳\n\nCafe name: {name}\nAddress: {address}\nEmail: {email}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(DEPARTURE_MAIL, PASS_DEPART_MAIL)
        connection.sendmail(from_addr=DEPARTURE_MAIL, to_addrs=ARRIVAL_MAIL, msg=email_message.encode('utf-8'))
