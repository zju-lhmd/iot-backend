class Config:
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wjwang:qwe987@127.0.0.1:3306/iot_backend'
    SQLALCHEMY_ECHO = False

    CORS_RESOURCES = {r'/api/*': {'origins': '*'}}


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/iot'
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/iot'
    SQLALCHEMY_ECHO = True


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
