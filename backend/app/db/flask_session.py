from flask_sqlalchemy import SQLAlchemy
from main import app  

# from db.base import Base
# Removed until Base is defined kwarg for SQLALCHEMY "model_class=Base"
# db = SQLAlchemy(app, model_class=Base)
db = SQLAlchemy()

db_session = db.session

def reset_database():
    from db.models import Post, Category  # noqa
    db.drop_all()
    db.create_all()
