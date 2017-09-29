#!/usr/bin/env python3
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db

app = create_app('default')
migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
