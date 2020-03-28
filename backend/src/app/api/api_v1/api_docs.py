# Import installed packages
# Import app code
from ...main import app

# from ...core import config

security_definitions = {
    "Bearer": {
        "type": "oauth2",
        "flow": "password",
        "tokenUrl": "/login/access-token",
        "in": "header",
    }
}

security_params = [{"Bearer": []}]
