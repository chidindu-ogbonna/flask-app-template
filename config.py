import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Base class for configurations """
    SECRET_KEY = 'a basic flask template for flask applications'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ Docstring for DevelopmentConfig """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'dev.db')


class TestingConfig(Config):
    """ Docstring for TestingConfig """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'test.db')


config = {
    'development' : DevelopmentConfig,
    'testing'     : TestingConfig,
    'default'     : DevelopmentConfig
}
