from flask import render_template, redirect, url_for

from . import main
from .. import db
from .. import modles

@main.route('/')
def index():
    return render_template('showMark.html')