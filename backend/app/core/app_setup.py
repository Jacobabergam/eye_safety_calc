#Import installed packages
from flask import Flask, Blueprint
from os import path
import logging
import logging.config

# Import app code
from main import app
from db.flask_session import db_session #one of these is not needed. Try to switch to db_session later
from db.flask_session import db
import core.config as config
from api.api_v1.api import api as api_instance

import api.api_v1.endpoints.posts
from api.api_v1.endpoints.posts import ns as blog_posts_namespace
from api.api_v1.endpoints.categories import ns as blog_categories_namespace
# Set up CORS
print(path.join(path.dirname(path.abspath(__file__))))

log_file_path = path.join(path.dirname(
    path.abspath(__file__)), 'log.conf')
logging.config.fileConfig(log_file_path)
log = logging.getLogger(__name__)

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = config.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = config.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = config.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = config.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = config.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api_instance.init_app(blueprint)
    api_instance.add_namespace(blog_posts_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


def main():
    initialize_app(app)
    log.info(
        '>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=config.FLASK_DEBUG)
