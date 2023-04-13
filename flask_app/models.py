from datetime import datetime
from flask_login import UserMixin
from . import db, login_manager


class Data(db.Model):
    """Data entries"""
    __tablename__ = 'Data'

    id = db.Column(db.Integer(), primary_key=True)
    Temperature = db.Column(db.Float(), nullable=False)
    Salinity = db.Column(db.Float(), nullable=False)
    Density = db.Column(db.Float(), nullable=False)
    Pressure = db.Column(db.Float(), nullable=False)
    Date = db.Column(db.Float(), nullable=False)
    Longitude = db.Column(db.Float(), nullable=False)
    Latitude = db.Column(db.Float(), nullable=False)
    Depth = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        """
        Returns the attributes of a data entry as a string
        :returns str
        """
        return f"Entry id {self.id}" 


class User(UserMixin, db.Model):
    """
    Database table for users
    Store username and password for logins
    Extra field to aid implementing more features in the future
    """
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)

    email = db.Column(db.String(255), unique=True, default=None)
    active = db.Column(db.Boolean(), default=True)
    confirmed_at = db.Column(db.DateTime(), default=datetime.now())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def check_credentials(username, password):
        """
        Helper function that returns the right user,
        if the password entered matches the user
        """
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return user
        else:
            return None


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()
