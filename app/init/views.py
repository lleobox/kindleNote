from flask import render_template, redirect, url_for, request, make_response, session

from . import init
from . import init_db
from .. import db
from .. import modles

@init.before_app_first_request
def first_init():
    init_db.init_db()

@init.route('/')
def loding():
    return redirect(url_for('main.index'))
