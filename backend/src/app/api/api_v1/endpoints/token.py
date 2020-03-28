# Import standard library
from datetime import timedelta

# Import installed modules
from flask import abort
from webargs import fields
from webargs.flaskparser import use_kwargs
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, get_current_user, jwt_required

# Import app code
from ..api import api
from app.api.api_v1.api_docs import security_definitions, security_params
from app.core.security import pwd_context, verify_password
from app.db.flask_session import db_session
from app.db.utils import get_user_by_username, get_user_hashed_password, get_user_id
from app.main import app

# Import schemas
from app.schemas.token import TokenSchema
from app.schemas.user import UserSchema

# Import models
from app.models.user import User

api = Namespace("login", description="Login Related Functions", validate=True,)

# parser = api.parser()
# parser.add_argument('Authorization', type=str,
#                 location='headers',
#                 help='Bearer Access Token',)

login_model = api.model(
    "login",
    {
        "username": fields.String("The Username", required=True),
        "password": fields.String("The Password", required=True),
    },
)

parser = api.parser()
parser.add_argument(
    "Authorization",
    type=str,
    location="headers",
    help="Bearer Access Token",
    required=True,
)

token_model = api.model(
    "token", {"access_token": fields.String(), "token_type": fields.String(),}
)

user_model = api.model(
    "user",
    {
        "id": fields.Integer(),
        "created_at": fields.DateTime(),
        "firest_name": fields.String(),
        "last_name": fields.String(),
        "email": fields.String(),
        "is_active": fields.Boolean(),
        "is_superuser": fields.Boolean(),
        "roles": fields.Nested(token_model, many=True),
    },
)


@api.route("/access-token")
@api.doc(
    description="OAuth2 compatible token login, get an access token for future requests",
    tags=["login"],
)
class RouteLoginAccessToken(Resource):
    """
    """

    @api.expect(login_model)
    @api.marshal_with(token_model)
    def post(self):
        print(api.header)
        payload = api.payload
        username = payload["username"]
        password = payload["password"]
        user = get_user_by_username(username, db_session)

        if not user or not verify_password(password, get_user_hashed_password(user)):
            abort(400, "Incorrect email or password")
        elif not user.is_active:
            abort(400, "Inactive user")
        access_token_expires = timedelta(minutes=60 * 24 * 8)
        return {
            "access_token": create_access_token(
                identity=get_user_id(user), expires_delta=access_token_expires
            ),
            "token_type": "bearer",
        }


@api.route("/test-token")
@api.doc(description="Test access token", tags=["login"], security=security_params)
# @api.header('Authorization: Bearer', 'JWT Token', required=True)
class RoutTestToken(Resource):
    """
    """

    @jwt_required
    def post(self):
        print(api.payload)
        current_user = get_current_user()
        if current_user:
            return current_user
        else:
            abort(400, "No user")
        return current_user


@api.route("/maual-test-toke")
@api.doc(
    description='Test access token manually, same as the endpoint to "Test access token" but copying and adding the Authorization: Bearer <token>',
    params={
        "Authorization": {
            "description": "Authorization HTTP header with JWT token, like: Authorization: Bearer asdf.qwer.zxcv",
            "in": "header",
            "type": "string",
            "required": True,
        }
    },
    tags=["login"],
)
class RouteManualTestToken(Resource):
    """
    """

    @jwt_required
    @api.marshal_with(user_model)
    @api.doc(parser=parser)
    def post(self):
        print(Resource)
        current_user = get_current_user()
        if current_user:
            return current_user
        else:
            abort(400, "No user")
        return current_user
