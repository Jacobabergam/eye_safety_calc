# Import standard library packages
from datetime import datetime

# Import installed packages
from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

# Import app code
from db.base_class import Base
from db.flask_session import db_session

print(db_session)


class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    body = Column(String)
    pub_date = Column(DateTime)

    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", backref=backref("posts", lazy="dynamic"))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return "<Post %r>" % self.title


class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %r>" % self.name
