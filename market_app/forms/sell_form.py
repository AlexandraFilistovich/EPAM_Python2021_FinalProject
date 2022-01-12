from flask_wtf import FlaskForm
from wtforms import SubmitField


class SellForm(FlaskForm):
    submit = SubmitField(label='Sell')
