from flask import Flask
from flask_admin import Admin
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from config import config

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
bootstrap = Bootstrap()
admin = Admin(name='APP', template_mode='bootstrap3')

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    # register blueprints
    from .views.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from .views.main import main
    app.register_blueprint(main)

    return app
