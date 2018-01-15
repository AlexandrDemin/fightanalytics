class ProductionConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:grillo@localhost/fightanalytics'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:grillo@localhost/fightanalytics'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
