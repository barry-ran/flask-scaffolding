from .home import home_bp
from .log_list import log_list_bp

def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(log_list_bp)