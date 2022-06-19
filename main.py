import datetime as dt
from flask import Flask, render_template


application = Flask(__name__)

year = dt.datetime.now().year

@application.route("/")
def home():
    return render_template("index.html", current_year=year)

@application.route("/about")
def about():
    return render_template("about.html", current_year=year)

@application.route("/contact")
def contact():
    return render_template("contact.html", current_year=year)

if __name__ == "__main__":
    application.run(debug=True)