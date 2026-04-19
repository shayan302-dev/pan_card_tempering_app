import os
from os import environ

class Config(object):
    DEBUG = False
    TESTING = False

    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = environ.get("SECRET_KEY", "shayan")

    UPLOAD_FOLDER = os.path.join(BASEDIR, "static", "uploads")

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class DebugConfig(Config):
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False
