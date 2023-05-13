# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent='minha-aplicacao')

# location = geolocator.geocode('Braga')

# print(location.latitude, location.longitude)

# import socket

# ip_local = socket.gethostbyname(socket.gethostname())
# print(f'IP Local: {ip_local}')

# import requests

# ip_publico = requests.get('https://api.ipify.org/').text
# print(f'IP Publico: {ip_publico}')

# import geocoder

# g = geocoder.ip('me')
# print(g.latlng)
# print(g.address)

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mcmlxxxiv',
    database='cafes_braga'
)
cursor = mydb.cursor()


# READ
command_read = 'SELECT * FROM cafes'
cursor.execute(command_read)
consulta = cursor.fetchall() # Lê e armazena a informação na variável indicada cRud
for linha in consulta:
    for item in linha[1:]:
        if item[:4] == 'http':
            print(item[7:])
        else:
            print(item)
cursor.close()
mydb.close()



# # CREATE
# command_create = f'INSERT INTO cafes (cafe_name, location, opening_time, closing_time, coffee_rating, wifi_signal, power) VALUES ("{cafe_name}", "{location}", "{opening}", "{closing}", {coffee_rating}, {wifi_signal}, {power})'
# cursor.execute(command_create)
# mydb.commit() # Para comandos que editam o banco de dados CrUD
# cursor.close()
# mydb.close()

## READ
# command_read = 'SELECT * FROM cafes'
# cursor.execute(command_read)
# consulta = cursor.fetchall() # Lê e armazena a informação na variável indicada cRud
# print(consulta)
# cursor.close()
# mydb.close()

## UPDATE
# power = 2
# cafe_name = "Café do Panda"

# command_update = f'UPDATE cafes SET power = {power} WHERE cafe_name = "{cafe_name}"'
# cursor.execute(command_update)
# mydb.commit() # Para comandos que editam o banco de dados CrUD
# cursor.close()
# mydb.close()

## DELETE
# comando_delete = f'DELETE FROM cafes WHERE cafe_id = 3'
# cursor.execute(comando_delete)
# mydb.commit() # Para comandos que editam o banco de dados CrUD
# cursor.close()
# mydb.close()
