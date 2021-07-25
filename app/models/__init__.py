
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_app(app):
    migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app)

    return db