import datetime as dt
from flask import Flask, render_template, request, redirect, url_for
from forms import NewLocation, RequestInclusion, CafeForm
from api import send_email, weather_checker, city_lat_long
import os
from dotenv import load_dotenv
import csv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')

# my_place = geocoder.ip('me').json
# current_city = my_place['city']
# current_latitude = my_place['lat']
# current_longitude = my_place['lng']

year = dt.datetime.now().year
weather = weather_checker()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_new_city = request.form
        new_city = form_new_city['city_name']
        new_lat, new_long, new_city_name, new_country = city_lat_long(new_city)
        new_weather = weather_checker(latitude=new_lat, longitude=new_long)
        return render_template("index.html", current_year=year, weather=new_weather, city_name=new_city_name, country=new_country)
    else:
        return render_template("index.html", current_year=year, weather=weather, city_name='Braga', country='PT')

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

@app.route("/add", methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit:
        with open(file='cafe-data.csv', mode='a') as list_cafes: # Include cafes database path into environment variable
            list_cafes.write(f'\n{form.cafe.data},{form.location.data},{form.opening_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi_signal.data},{form.power.data}')
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
