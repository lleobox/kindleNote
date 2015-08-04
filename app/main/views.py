from flask import render_template, redirect, url_for

from . import main
from .. import db
from .. import modles

@main.route('/')
def index():
    mark = modles.Mark.query.all()
    return render_template('showMark.html', mark=mark)

@main.route('/delete=<id>')
def delete(id):
    mark = modles.Mark.query.filter_by(id=id).first()
    if mark is not None:
        db.session.delete(mark)
        return '目录删除成功'