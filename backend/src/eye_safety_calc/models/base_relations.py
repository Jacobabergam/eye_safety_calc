# Import installed packages
from sqlalchemy import Table, Column, Integer, ForeignKey

# Import app code
from db.base_class import Base

user_roles = Table(
    "users_roles",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("role_id", Integer, ForeignKey("role.id")),
)