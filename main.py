import datetime as dt
from flask import Flask, render_template


app = Flask(__name__)

year = dt.datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", current_year=year)

@app.route("/about")
def about():
    return render_template("about.html", current_year=year)

@app.route("/contact")
def contact():
    return render_template("contact.html", current_year=year)

if __name__ == "__main__":
    app.run(debug=True)