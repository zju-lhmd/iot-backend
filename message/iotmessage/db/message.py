from .db import db


class Message(db.Model):
    # 数据表名
    __tablename__ = 'message'
    # 数据表属性定义
    message_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    device_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    alert = db.Column(db.Integer, nullable=False)
    info = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Double, nullable=False)
    longitude = db.Column(db.Double, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    # 一般信息键
    info_keys = ['message_id', 'device_id', 'timestamp', 'alert', 
                 'info', 'latitude', 'longitude', 'value']

    def __init__(self, message_id=None, device_id=None, timestamp=None, alert=None, info=None, latitude=None, longitude=None, value=None):
        self.message_id = message_id
        self.device_id = device_id
        self.timestamp = timestamp
        self.alert = alert
        self.info = info
        self.latitude = latitude
        self.longitude = longitude
        self.value = value

    def __repr__(self):
        return f'<Message {self.message_id!r} {self.device_id!r} {self.timestamp!r} {self.alert!r} {self.info!r} {self.latitude!r} {self.longitude!r} {self.value!r}>'

    def get(self):
        info = {}
        for key in self.info_keys:
            info[key] = self.__getattribute__(key)
        return info
