import os

from config import basedir
from app import create_app, db
from app.modles import Mark, Note
from flask.ext.script import Manager, Shell
from flask.ext.migrate import MigrateCommand
from app.init.init_db import init_db



app = create_app('development')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Mark=Mark, Note=Note, init=init_db)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
