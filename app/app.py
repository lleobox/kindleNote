from flask import Flask, request, redirect, render_template, url_for, session, g, abort, flash
import sqlite3

app = Flask(__name__)

def connetc_db():
    '''Connects to the database'''
    conn = sqlite3.connect('db.db')
    cour = conn.cursor()
    return cour

def get_db():
    """Closes the database again at the end of the request."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connetc_db()
    return g.sqlite_db

def close_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def showMark():
    # todo: 完成数据库列表的导出
    db = get_db()
    cur = db.execute('select id,name,content from book order by id')
    entries = cur.fetchall()
    return render_template('showMark.html', items=entries)


@app.route('/note')
def showNote():
    return render_template('showNote.html')


@app.route('/about')
def showAbout():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
