import requests

# print(requests.get('https://ipinfo.io').content)

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='minha-aplicacao')

location = geolocator.geocode('Helsinki')

print(location)
