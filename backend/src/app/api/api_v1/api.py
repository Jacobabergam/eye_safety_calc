# Import installed packages
from flask_restx import Api

# Import app code
from app.main import app

# from app.core import config
from app.db.flask_session import db_session

from .api_docs import security_definitions, security_params

api = Api(
    app=app,
    version="1.0",
    title="Test API",
    description="A Simple Test API",
    authorizations=security_definitions,
    security=security_params,
)

from .endpoints.role import api as ns_role
from .endpoints.token import api as ns_token  # noqa
from .endpoints.user import api as ns_user  # noqa

# from .endpoints import utils as ns_util # This is used to test celery


api.add_namespace(ns_role)
api.add_namespace(ns_token)
api.add_namespace(ns_user)
# api.add_namespace(ns_util) # This is used to test celery
