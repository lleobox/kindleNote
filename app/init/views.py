from flask import render_template, redirect, url_for, request, make_response

from . import init
from .. import db
from .. import modles

@init.route('/init')
def init():
    return render_template('init.html')

