import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # falsk的内置config key: https://flask.palletsprojects.com/en/2.0.x/config/
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # init_app是为了在初始化app时附加一些额外配置用的
    @classmethod
    def init_app(cls, app):
        print(cls.SQLALCHEMY_DATABASE_URI)
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.db')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}