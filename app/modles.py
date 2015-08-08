from flask.ext.sqlalchemy import SQLAlchemy
from . import db
from time import time

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

class Note(db.Model):
    __tablename__ = 'Note'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    mark = db.Column(db.Text)
    note = db.Column(db.Text)
    date = db.Column(db.Date)

    def __init__(self, name, mark, note):
        self.name = name
        self.mark = mark
        self.note = note
        self.date = time()

    def __repr__(self):
        return '<Note %r>:' % self.id