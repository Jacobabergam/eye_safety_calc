# Import installed packages
from apispec import APISpec
from flask_apispec import FlaskApiSpec

# Import app code
from main import app
from eye_safety_calc.config import Config

security_definitions = {
    "bearer": {
        "type": "oauth2",
        "flow": "password",
        "tokenUrl": f"{Config.API_V1_STR}/login/access-token",
    }
}

app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title=Config.PROJECT_NAME,
            version="v1",
            plugins=("apispec.ext.marshmallow",),
            securityDefinitions=security_definitions,
        ),
        "APISPEC_SWAGGER_URL": f"{Config.API_V1_STR}/swagger/",
    }
)
docs = FlaskApiSpec(app)

security_params = [{"bearer": []}]
