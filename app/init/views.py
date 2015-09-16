from flask import render_template, redirect, url_for, request, make_response, session
from datetime import timedelta

from . import init
from . import init_db
from .. import db
from .. import modles


@init.route('/')
def loding():
    if request.cookies.get('expir') == 'true':
        return redirect('selectbook')
    else:
        init_db.init_db()
        resp = make_response(redirect('selectbook'))
        resp.set_cookie('expir', 'true', max_age=1800)
        return resp
