import datetime as dt
from flask import Flask, render_template, request, redirect, url_for
from forms import NewLocation, RequestInclusion, CafeForm, DeleteForm
from api import send_email, weather_checker, city_lat_long
import os
from dotenv import load_dotenv
import sqlite3



load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')

connection = sqlite3.connect("db/bragas-cafe.db")
cursor = connection.cursor()

year = dt.datetime.now().year
weather_id, weather, temperature = weather_checker()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_new_city = request.form
        new_city = form_new_city['city_name']
        new_lat, new_long, new_city_name, new_country = city_lat_long(new_city)
        new_weather_id, new_weather, new_temperature = weather_checker(latitude=new_lat, longitude=new_long)
        return render_template("index.html", current_year=year, weather_id=new_weather_id, weather=new_weather, temperature=round(new_temperature), city_name=new_city_name, country=new_country)
    else:
        return render_template("index.html", current_year=year, weather_id=weather_id, weather=weather, temperature=round(temperature), city_name='Braga', country='PT')

@app.route("/about")
def about():
    return render_template("about.html", current_year=year)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = RequestInclusion()
    if request.method == 'POST':
        data = request.form
        send_email(data['cafe_name'], data['address'], data['email'])
        return render_template("successfully_request.html", current_year=year, form=form)
    return render_template("contact.html", current_year=year, form=form)

@app.route("/success", methods=["GET", "POST"])
def success():
    return render_template("successfully_request.html", current_year=year)

@app.route("/change-location")
def change_location():
    form = NewLocation()
    return render_template("change_location.html", form=form)

###############################
## FUNCION TO ADD A NEW CAFE ##
###############################

@app.route('/cafes')
def cafes():
    # READ
    connection = sqlite3.connect("db/bragas-cafe.db")
    cursor = connection.cursor()
    command_read = 'SELECT * FROM cafes'
    cursor.execute(command_read)
    consulta = cursor.fetchall() # Lê e armazena a informação na variável indicada cRud
    cursor.close()
    connection.close()
    return render_template('cafes.html', cafes=consulta)

###############################
## FUNCTION TO DELETE A CAFE ##
###############################

# if __name__ == "__main__":
#     app.run(debug=True, port=5000, host="0.0.0.0")
