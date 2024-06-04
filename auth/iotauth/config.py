class Config:
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://iot:iot@127.0.0.1:3306/iot_backend'
    SQLALCHEMY_ECHO = False

    CORS_RESOURCES = {r'/api/*': {'origins': '*'}}


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/iot'
    SQLALCHEMY_ECHO = True


class LocalTestConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/iot'
    SQLALCHEMY_ECHO = True


class RemoteTestConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://iot:iot@127.0.0.1:3306/iot_backend'
    SQLALCHEMY_ECHO = True


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'local_test': LocalTestConfig,
    'remote_test': RemoteTestConfig,
}
