from flask import render_template, redirect, url_for

from . import main
from .. import db
from .. import modles

@main.route('/')
def index():
    mark = modles.Mark.query.all()
    return render_template('showMark.html', mark=mark)