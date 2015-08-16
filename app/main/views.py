from flask import render_template, redirect, url_for, request, make_response

from . import main
from .. import db
from .. import modles

@main.route('/')
def index():
    mark = modles.Mark.query.all()
    return render_template('showMark.html', mark=mark)

@main.route('/showNote')
def showNote():
    return render_template('showNote.html')

@main.route('/delete=<id>')
def delete(id):
    mark = modles.Mark.query.filter_by(id=id).first()
    if mark is not None:
        db.session.delete(mark)
        return '目录删除成功'

@main.route('/addnote', methods=['POST', 'GET'])
def addNote():
    if request.method == 'GET':
        return redirect('404')
    note = modles.Note(request.form['name'], request.form['mark'], request.form['note'])
    try:
        db.session.add(note)
        return 'ok'
    except:
        return 'error'

