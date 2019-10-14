import os

class BaseConfig:
    """Base Configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Developement Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """Testing Configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProdcutionConfig(BaseConfig):
    """Production COnfig""" 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


