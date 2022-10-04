import datetime as dt
from flask import Flask, render_template
from forms import RequestInclusion
from api import weather_checker
import os

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')
year = dt.datetime.now().year
weather, weather_icon = weather_checker()

@app.route("/")
def home():
    return render_template("index.html", current_year=year, weather=weather, icon=weather_icon)


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


if __name__ == "__main__":
    app.run(debug=True)
