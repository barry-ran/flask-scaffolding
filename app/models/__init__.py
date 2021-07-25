
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_app(app):
    migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app)

    # 数据库不存在则创建
    with app.app_context():
        db.create_all()
    
    return db