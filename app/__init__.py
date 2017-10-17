from flask import Flask
from flask_admin import Admin
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

from config import config

db = SQLAlchemy()
mail = Mail()
security = Security()
admin = Admin(name='APP', template_mode='bootstrap3')


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    from .models import User
    datastore = SQLAlchemyUserDatastore(db, User)
    security.init_app(app, datastore)
    # If using this with an external application like "celery"
    #  security_ctx = security.init_app(app, datastore)

    # register blueprints
    from .views.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from .views.main import main
    app.register_blueprint(main)

    return app
