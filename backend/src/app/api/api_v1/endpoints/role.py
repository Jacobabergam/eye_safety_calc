# Import standard library modules

# Import installed modules
from flask import abort
from webargs import fields
from webargs.flaskparser import use_kwargs
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import get_current_user, jwt_required

# Import app code
from app.main import app
from app.api.api_v1.api_docs import security_params
from app.db.flask_session import db_session
from app.db.utils import (
    check_if_user_is_active,
    check_if_user_is_superuser,
    get_role_by_name,
    create_role,
    get_roles,
    get_user_roles,
)

# Improt Schemas
from app.schemas.role import RoleSchema
from app.schemas.msg import MsgSchema

# Import models
from app.models.role import Role
from app.models.user import User

api = Namespace("roles", description="Role related Functions", validate=True,)

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

role_model = api.model(
    "role",
    {
        "id": fields.Integer(),
        "created_at": fields.DateTime(),
        "name": fields.String(),
        "users": fields.Nested(
            user_model,
            only=["id", "first_name", "last_name", "email", "is_active", "is_superuser"],
            many=True,
        ),
    },
)


@api.route("/")
@api.doc(description="Role related functions")
class RouteRoles(Resource):
    """
    """

    @jwt_required
    @api.marshal_with(role_model)
    def post(self):
        name = api.payload["name"]
        current_user = get_current_user()
        if not current_user:
            abort(400, "Could not authenticate user with provided token")
        elif not check_if_user_is_active(current_user):
            abort(400, "Inactive user")
        elif not check_if_user_is_superuser(current_user):
            abort(400, "Not a superuser")

        role = get_role_by_name(name, db_session)
        if role:
            return abort(400, f"The role: {name} already exists in the system")
        role = create_role(name, db_session)
        return role

    @api.doc(
        description="Retrieve the roles of the user",
        security=security_params,
        tags=["roles"],
    )
    @jwt_required
    @api.marshal_with(role_model)
    def get(self):
        current_user = get_current_user()  # type: User
        if not current_user:
            abort(400, "Could not authenticate user with provided token")
        elif not check_if_user_is_active(current_user):
            abort(400, "Inactive user")

        if check_if_user_is_superuser(current_user):
            return get_roles(db_session)
        else:
            return get_user_roles(current_user)
