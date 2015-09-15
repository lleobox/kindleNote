from flask import render_template, redirect, url_for, request, make_response

from . import main
from .. import db
from .. import modles



@main.route('/showMark')
def index():
    mark = modles.Mark.query.order_by(modles.Mark.id.desc())
    return render_template('showMark.html', mark=mark)

@main.route('/showNote')
def showNote():
    note = modles.Note.query.all()
    return render_template('showNote.html', note=note)

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

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/delete=<id>')
def delete(id):
    mark = modles.Mark.query.filter_by(id=id).first()
    if mark is not None:
        db.session.delete(mark)
        return '目录删除成功'

