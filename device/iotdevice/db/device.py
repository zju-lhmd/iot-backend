from sqlalchemy import UniqueConstraint

from .db import db


class Device(db.Model):
    # 数据表名
    __tablename__ = 'device'
    # 数据表属性定义
    device_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    device_name = db.Column(db.String(50), nullable=False)
    device_type = db.Column(db.String(20), nullable=False)
    creator = db.Column(db.String(20), nullable=False)
    online = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    last_update_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(100), nullable=True)
    # 一般信息键
    info_keys = ['device_id', 'device_name', 'device_type', 'creator', 'online', 
                 'creation_date', 'last_update_date', 'description']
    # 添加唯一约束
    __table_args__ = (UniqueConstraint('device_name', 'device_type', 'creator', name='_device_uc'),)

    def __init__(self, device_id=None, device_name=None, device_type=None, creator=None, online=0, creation_date=None, description='无'):
        self.device_id = device_id
        self.device_name = device_name
        self.device_type = device_type
        self.creator = creator
        self.online = online
        self.creation_date = creation_date
        self.last_update_date = creation_date
        self.description = description

    def __repr__(self):
        return f'<Device {self.device_id!r} {self.device_name!r} {self.device_type!r} {self.creator!r} {self.online!r} {self.creation_date!r} {self.last_update_date!r} {self.description!r}>'

    def get(self):
        info = {}
        for key in self.info_keys:
            info[key] = self.__getattribute__(key)
        return info
