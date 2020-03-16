from flask_sqlalchemy import SQLAlchemy
import app
from db.base import Base

db = SQLAlchemy(app, model_class=Base)
db_session = db.session


db = SQLAlchemy()


def reset_database():
    from database.models import Post, Category  # noqa
    db.drop_all()
    db.create_all()
