# Import Installed Packages
from flask import Flask
from flask_restplus import Api

#Import app code
from main import app
from core import config
from db.flask_session import db, db_session


api = Api(version='1.0', title='Eye Safety Calculator API',
          description='An API for creating a laser system',
          )
