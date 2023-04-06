from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import DataRequired


class PredictionForm(FlaskForm):
    """Form fields to input the values required to predict temperture"""

    Date = DecimalField(validators=[DataRequired()])
    
    