## Import standard library modules
import uuid

# Import Installed packages
from flask import abort
from webargs import fields
from webargs.flaskparser import use_kwargs
from flask_restx import Namespace, Resource, fields


# Import app code
from ..api import api
from app.db.flask_session import db_session
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

# Import Schemas
from app.schemas.user import UserSchema

# Import models
from app.models.user import User

api = Namespace("user", description="User Rleated Operations")

#
a_User = api.model(
    "User",
    {
        "username": fields.String("The Username", required=True),
        "password": fields.String("The Password", required=True),
        "first_name": fields.String("First Name"),
        "last_name": fields.String("Last Name"),
        # 'uid' : fields.Integer(readOnly=True, description='The unique id number')
    },
)


@api.route("/")
@api.doc(params={"username": "a unique user name documented using api.doc"})
class User(Resource):
    def get(self):
        schema = UserSchema(many=True)

        return schema.dump(db_session)

    @api.expect(a_User)
    @api.doc(responses={403: "Not Authorized"})
    def post(self):
        new_user = api.payload
        new_user["uid"] = uuid.uuid4()
        db.append(new_user)
        return {"result": "New User created"}, 201


@api.route("/open")
@api.doc(
    params={
        "email": "User email",
        "password": "User password",
        "first_name": "Users first name",
        "last_name": "Users last name",
    }
)
class UserOpen(Resource):
    """
    route_users_post_open    
    """

    @api.expect(a_User)
    def post(self, username=None, password=None, first_name=None, last_name=None):
        # if not config.USERS_OPEN_REGISTRATION:
        #     abort(403, "Open user resgistration is forbidden on this server")

        payload = api.payload
        username = payload["username"]
        user = get_user(username, db)

        if user:
            return abort(
                400, f"The user with this email already exists in the system: {username}"
            )

        # user = create_user(db, username, password, first_name, last_name)
        payload["uid"] = uuid.uuid4()
        db.append(payload)
        return {"result": "New User created"}, 201
        # return payload # Does this require JWT?
