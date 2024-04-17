from AuthMicroservices.db import db


class Account(db.Model):
    # 数据表名
    __tablename__ = 'account'
    # 数据表属性定义
    username = db.Column(db.String(32), nullable=False, primary_key=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(32), nullable=False, unique=True)
    phone = db.Column(db.String(32), nullable=False)
    # 一般信息键
    info_keys = ['username', 'email', 'phone']

    def __init__(self, username=None, password=None, email=None, phone=None):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f'<Account {self.username!r} {self.email!r} {self.phone!r}>'

    def get(self):
        info = {}
        for key in self.info_keys:
            info[key] = self.__getattribute__(key)
        return info
