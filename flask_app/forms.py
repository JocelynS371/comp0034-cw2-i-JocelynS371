from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    Username = DecimalField(validators=[DataRequired()])
    Password = DecimalField(validators=[DataRequired()])



class PredictionForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    date = DecimalField(validators=[DataRequired()])
    longtitude = DecimalField(validators=[DataRequired()])
    latitude = DecimalField(validators=[DataRequired()])
    
    