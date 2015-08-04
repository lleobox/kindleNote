from flask.ext.sqlalchemy import SQLAlchemy
from . import db

class Mark(db.Model):
    __tablename__ = 'Mark'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    position = db.Column(db.Text)
    date = db.Column(db.Text)
    content = db.Column(db.Text)

    def __init__(self, name, position, date, content):
        self.name = name
        self.position = position
        self.date = date
        self.content = content

    def __repr__(self):
        return '<Mark %r>' % self.id
