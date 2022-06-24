from ast import Sub
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email


class RequestInclusion(FlaskForm):
    cafe_name = StringField(label='Cafe name:', validators=[DataRequired()])
    address = StringField(label='Address:', validators=[DataRequired()])
    email = EmailField(label='E-mail:', validators=[Email()])
    submit = SubmitField(label='Send request')
