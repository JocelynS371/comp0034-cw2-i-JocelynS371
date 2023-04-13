from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, FloatField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

class UserForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=
    [
        DataRequired(),
        Length(min=6, message='Password too short, must be at least %(min)d charater long')
        ])
    password_verif = PasswordField('Confirm Password', validators=
    [
        DataRequired(),
        EqualTo('password'),
        ])

class LoginForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])



class PredictionForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    date = DecimalField(validators=[DataRequired()])
    longtitude = FloatField(validators=[DataRequired()])
    latitude = FloatField(validators=[DataRequired()])
    
    