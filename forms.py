from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email


class RequestInclusion(FlaskForm):
    cafe_name = StringField(label='Cafe name:', validators=[DataRequired()])
    address = StringField(label='Address:', validators=[DataRequired()])
    email = EmailField(label='E-mail:')
    submit = SubmitField(label='Come visit me')

class NewLocation(FlaskForm):
    city_name = StringField(label='City name:', validators=[DataRequired()])
    submit = SubmitField(label='Show that city, please.')
