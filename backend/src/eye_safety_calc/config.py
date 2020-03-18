"""Config variables
"""
import os

# Flask settings
FLASK_SERVER_NAME = "localhost:8888"
FLASK_DEBUG = True  # Do not use debug mode in production
LOG_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.cfg")

# Flask-Restplus settings
PROJECT_NAME = "Test Area"
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = "list"
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
API_V1_STR = "/api/v1"

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = False
