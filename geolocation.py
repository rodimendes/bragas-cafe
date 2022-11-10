# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent='minha-aplicacao')

# location = geolocator.geocode('Braga')

# print(location.latitude, location.longitude)

import socket

ip_local = socket.gethostbyname(socket.gethostname())
print(f'IP Local: {ip_local}')

import requests

ip_publico = requests.get('https://api.ipify.org/').text
print(f'IP Publico: {ip_publico}')

import geocoder

g = geocoder.ip('me')
print(g.latlng)
print(g.address)
