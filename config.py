import os
import random, string 

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = 'b_5#y2L"F4Q8z/n\xec]/'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8081
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

#app_active = os.getenv('FLASK_ENV') aqui é para passar a variável de ambiente no 
app_active = 'development'


