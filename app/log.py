import os
import logging
from logging import handlers
from werkzeug.exceptions import InternalServerError

basedir = os.path.abspath(os.path.dirname(__file__))

def handle_error(error):
    Log.logger().error(error)
    return error

class Log:
    LOG_PATH = os.path.join(basedir, 'logs')
    LOG_NAME = os.path.join(LOG_PATH, 'app.log')
    LOG_LEVEL = 'INFO'

    current_app = None

    @staticmethod
    def init_app(app):
        Log.current_app = app
        if not os.path.exists(Log.LOG_PATH):
            os.makedirs(Log.LOG_PATH)

        # 根据时间重命名log
        file_handler = logging.handlers.TimedRotatingFileHandler(Log.LOG_NAME, when='D', interval=1, backupCount=0, encoding='utf-8')
        file_handler.suffix = '%Y-%m-%d.log'
        # 单独设置handler的日志级别：低于该级别则该handler不处理（一个logger可以有多个handler）
        # file_handler用来写入文件
        file_handler.setLevel(Log.LOG_LEVEL)

        fmt = '%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-%(lineno)s: %(message)s'
        formatter = logging.Formatter(fmt)
        file_handler.setFormatter(formatter)

        # 设置logger的日志级别：大于等于该级别才会交给handler处理
        app.logger.setLevel('DEBUG')
        app.logger.addHandler(file_handler)

        # DEBUG模式下不会走到handle_error
        app.register_error_handler(InternalServerError, handle_error)

    @staticmethod
    def logger():
        return Log.current_app.logger