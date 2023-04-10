from . import db
import datetime


class data(db.Model):

    """ data entries"""

    __tablename__ = 'data'
    index = db.Column(db.Integer(), primary_key = True)
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

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    def check_credentials(username, password):
        User = user.query.filter_by(username=username).first()
        if User.password == password:
            return True
        else: return False