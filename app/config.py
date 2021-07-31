import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

class Config:
    # falsk的内置config key: https://flask.palletsprojects.com/en/2.0.x/config/
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    PRODUCTION_CONFIG = False

    # init_app是为了在初始化app时附加一些额外配置用的
    @classmethod
    def init_app(cls, app):
        pass

class DevelopmentConfig(Config):
    # 设置了FLASK_ENV环境变量自动是DEBUG模式
    # DEBUG = True
    # 没有指定DEV_DATABASE_URL则使用sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO= True
    PRODUCTION_CONFIG = False

class ProductionConfig(Config):
    # 没有指定DATABASE_URL则使用sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')
    PRODUCTION_CONFIG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}