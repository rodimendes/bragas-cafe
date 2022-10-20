import datetime as dt
from flask import Flask, render_template, request
from forms import NewLocation, RequestInclusion
from api import weather_checker, city_lat_long
import os
import geocoder
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')

my_place = geocoder.ip('me').json
current_city = my_place['city']
current_latitude = my_place['lat']
current_longitude = my_place['lng']

year = dt.datetime.now().year
weather = weather_checker(latitude=current_latitude, longitude=current_longitude)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_new_city = request.form
        new_city = form_new_city['city_name']
        new_lat, new_long, new_city_name, new_country = city_lat_long(new_city)
        new_weather = weather_checker(latitude=new_lat, longitude=new_long)
        return render_template("index.html", current_year=year, weather=new_weather, city_name=new_city_name, country=new_country)
    return render_template("index.html", current_year=year, weather=weather, city_name=current_city)


@app.route("/about")
def about():
    return render_template("about.html", current_year=year)


@app.route("/contact")
def contact():
    form = RequestInclusion()
    return render_template("contact.html", current_year=year, form=form)


@app.route("/success", methods=["GET", "POST"])
def success():
    return render_template("successfully_request.html", current_year=year)


@app.route("/change-location")
def change_location():
    form = NewLocation()
    return render_template("change_location.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
