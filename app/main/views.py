from flask import render_template, sessions, redirect, url_for

from . import main
from .. import db
from .. import modles

@main.route('/')
def index():
    return 'hello!'