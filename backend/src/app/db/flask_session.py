from flask_sqlalchemy import SQLAlchemy

from app.main import app

# from app.core import config
from app.db.base import Base

TEST_SQLALCHEMY_DATABASE_URI = "sqlite:///test.sqlite"

# app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_DATABASE_URI"] = TEST_SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app, model_class=Base)
db.create_all()
db_session = db.session
