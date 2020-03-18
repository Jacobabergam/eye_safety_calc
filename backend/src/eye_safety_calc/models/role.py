""" Manages user permissions within the app """
# Import standard library packages
from datetime import datetime

# Import installed packages
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship

# Import app code
from db.base_class import Base
from models.base_relations import user_roles


class Role(Base):
    # Own properties
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow(), index=True)
    name = Column(String, index=True)
    # Relationships
    users = relationship("User", secondary=user_roles, back_populates="roles")
