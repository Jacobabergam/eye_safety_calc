"""Config settings for for development, testing and production environments."""
import os
from pathlib import Path

HERE = Path(__file__).parent
SQLITE_DEV = "sqlite:///" + str(HERE / "eye_safety_calc_dev.db")
SQLITE_TEST = "sqlite:///" + str(HERE / "eye_safety_calc_test.db")
SQLITE_PROD = "sqlite:///" + str(HERE / "eye_safety_calc_prod.db")


class Config:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "open sesame")
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False

    # TEST ADDED BELOW
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


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = SQLITE_TEST


class DevelopmentConfig(Config):
    """Development configuration."""

    TOKEN_EXPIRE_MINUTES = 15
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_DEV)


class ProductionConfig(Config):
    """Production configuration."""

    TOKEN_EXPIRE_HOURS = 1
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_PROD)
    PRESERVE_CONTEXT_ON_EXCEPTION = True


ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
