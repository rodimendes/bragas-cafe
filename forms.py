from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, URL


class RequestInclusion(FlaskForm):
    cafe_name = StringField(label='Cafe name:', validators=[DataRequired()])
    address = StringField(label='Address:', validators=[DataRequired()])
    email = EmailField(label='E-mail:', validators=[DataRequired(), Email()])
    submit = SubmitField(label='Come visit me')

class NewLocation(FlaskForm):
    city_name = StringField(label='City name:', validators=[DataRequired()])
    submit = SubmitField(label='Show that city, please.')

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Address', validators=[DataRequired(), Length(min=15), URL()])
    opening_time = StringField('Open', validators=[DataRequired()])
    closing_time = StringField('Close', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee', choices=[(0, '❌'), (1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'), (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')]) # Pode ser colocado (1, '❌'). Assim, o valor atribuído é a chave do par chave-valor
    wifi_signal = SelectField('Wifi', choices=[(0, '❌'), (1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')])
    power = SelectField('Power', choices=[(0, '❌'), (1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')])
    # contact = StringField('Your best e-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
