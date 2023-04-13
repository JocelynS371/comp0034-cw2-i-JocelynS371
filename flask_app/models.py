from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin

class Data(db.Model):

    """ data entries"""

    __tablename__ = 'Data'
    id = db.Column(db.Integer(), primary_key = True)
    Temperture = db.Column(db.Float(), nullable = False)
    Salinity = db.Column(db.Float(), nullable = False)
    Density = db.Column(db.Float(), nullable = False)
    Pressure = db.Column(db.Float(), nullable = False)
    Date = db.Column(db.Float(), nullable = False)
    Longitude = db.Column(db.Float(), nullable = False)
    Latitude = db.Column(db.Float(), nullable = False)
    Depth = db.Column(db.Float(), nullable = False)

    def __repr__(self):
        """
        Returns the attributes of an data entry as a string
        :returns str
        """
        clsname = self.__class__.__name__
        return f"Entry id {self.entry_id}: {datetime.fromordinal(int(self.Date))}, {self.Longitude}, {self.Latitude}, {self.Temperture}, {self.Salinity}>"
    

class User(UserMixin,db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)

    email = db.Column(db.String(255), unique=True, default=None)
    active = db.Column(db.Boolean(), default=True)
    confirmed_at = db.Column(db.DateTime(), default=datetime.now())
    roles = db.relationship('Role', secondary='roles_users',
                            back_populates="users")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
    def check_credentials(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return user
        else: return None
    @login_manager.user_loader
    def load_user(id):
        return User.query.filter_by(id = id).first()



