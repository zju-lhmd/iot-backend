class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/iot'
    SQLALCHEMY_ECHO = False


class DevelopmentConfig(Config):
    DEBUG = True    # 启用调试模式(目前似乎没效果)
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
