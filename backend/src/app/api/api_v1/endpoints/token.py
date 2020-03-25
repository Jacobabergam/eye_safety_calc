# Import standard library
from datetime import timedelta

# Import installed modules
from flask import abort
from webargs import fields
from webargs.flaskparser import use_kwargs
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, get_csrf_token, jwt_required

# Import app code
from ..api import api
from app.db.flask_session import db
from app.core.security import pwd_context
from app.db.utils import (
    get_user,
    check_if_user_is_active,
    check_if_user_is_superuser,
    get_users,
    get_user_by_username,
    create_user,
    get_user_by_id,
    get_role_by_id,
    assign_role_to_user,
)

from app.main import app

# Import schemas
from app.schemas.token import TokenSchema
from app.schemas.user import UserSchema

# Import models
from app.models.user import User

api = Namespace(
    "login",
    description="OAuth2 compatible token login, get access token for future requests",
)

a_login = api.model(
    "User",
    {
        "username": fields.String("The Username", required=True),
        "password": fields.String("The Password", required=True),
    },
)


@api.route("/access-token")
@api.doc(
    description="OAuth2 compatible token login, get an access token for future requests",
    tags=["login"],
)
class RouteLoginAccessToekn(Resource):
    """
    """

    @api.expect(a_login)
    # @api.marshal_with(TokenSchema())
    def post(self):
        return
