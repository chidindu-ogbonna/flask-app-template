import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Base class for configurations """
    SECRET_KEY = 'a basic flask template for flask applications'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # mail configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # flask_security configuration
    SECURITY_EMAIL_SENDER = ''
    SECURITY_CONFIRMABLE = True  # adding a confirmed_at feature to the user model
    SECURITY_TRACKABLE = True  # adding tracking of tthe user usage

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ Docstring for DevelopmentConfig """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        BASE_DIR, 'data-dev.db')


class TestingConfig(Config):
    """ Docstring for TestingConfig """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        BASE_DIR, 'data-test.db')


class ProductionConfig(Config):
    """ Docstring for ProductionConfig """
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
