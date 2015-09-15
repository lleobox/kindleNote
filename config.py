import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = 'lleohao'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev-db.sqlite')
    SQLALCHEMY_BINDS = {
        'Mark': 'sqlite:///' + os.path.join(basedir, 'dev-mark.sqlite')
    }


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_BINDS = {
        'Mark': 'sqlite:///' + os.path.join(basedir, 'mark.sqlite')
    }


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db-back.sqlite')
    SQLALCHEMY_BINDS = {
        'Mark': 'sqlite:///' + os.path.join(basedir, 'test-mark.sqlite')
    }

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestingConfig,

    'default': DevelopmentConfig
}
