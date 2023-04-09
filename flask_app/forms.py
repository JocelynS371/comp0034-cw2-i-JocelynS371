from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, FloatField, PasswordField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])



class PredictionForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    date = DecimalField(validators=[DataRequired()])
    longtitude = FloatField(validators=[DataRequired()])
    latitude = FloatField(validators=[DataRequired()])
    
    