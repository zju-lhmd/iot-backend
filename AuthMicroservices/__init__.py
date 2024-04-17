from flask import Flask

from .config import config


def create_app(config_type='development'):
    # 构造Flask实例
    app = Flask(__name__)
    app.config.from_object(config[config_type])

    # 绑定数据库
    from .db import db
    db.init_app(app)

    # 初始化数据库
    with app.app_context():
        db.create_all()

    # 绑定控制器
    from .blueprints import account
    app.register_blueprint(account, url_prefix='/api')

    return app
