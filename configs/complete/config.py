import os

class Config(object):
    DEBUG = False
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(os.getcwd()) + "\\database.db"

class DevelopmentConfig(Config):
    DEBUG = True