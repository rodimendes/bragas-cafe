import datetime as dt
from flask import Flask, render_template
from forms import RequestInclusion


app = Flask(__name__)
app.secret_key = 'key_to_change'
year = dt.datetime.now().year


@app.route("/")
def home():
    return render_template("index.html", current_year=year)


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
