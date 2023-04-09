from flask_app import db


class data(db.model):

    """ data entries"""

    __tablename__ = 'data'
    entry_id = db.column(db.Interger, primary_key = True)