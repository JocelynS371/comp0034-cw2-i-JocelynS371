from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])



class PredictionForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    date = DecimalField(validators=[DataRequired()])
    longtitude = DecimalField(validators=[DataRequired()])
    latitude = DecimalField(validators=[DataRequired()])
    
    