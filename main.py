from crypt import methods
import datetime as dt
from flask import Flask, render_template, request
from forms import NewLocation, RequestInclusion
from api import weather_checker
import os


app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')
year = dt.datetime.now().year
weather, weather_icon = weather_checker()

@app.route("/", methods=['GET', 'POST'])
def home():
    city = request.form
    print(city.keys)
    return render_template("index.html", current_year=year, weather=weather, city_name=city)


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
