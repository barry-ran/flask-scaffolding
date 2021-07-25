from flask import Flask
from . import routes, models
from .config import config

# flask run命令会自动调用create_app函数 https://dormousehole.readthedocs.io/en/latest/cli.html
# 通过flask run启动时，可以通过设置FLASK_APP=app:create_app('development')来指定create_app的参数
def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    models.init_app(app)
    routes.init_app(app)

    return app