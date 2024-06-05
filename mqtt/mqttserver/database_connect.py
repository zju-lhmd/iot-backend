from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, TIMESTAMP, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import UniqueConstraint

from datetime import datetime
import time
import random

# python2: MySQLdb
# python3: pymysql
# 使用create_engine建立同数据库的连接，返回的是一个Engine实例
# 指向数据库的一些核心的接口
# echo=True， 可以在控制台看到操作涉及的SQL语言


# 声明基类
Base = declarative_base()


# 基于这个基类来创建我们的自定义类，一个类就是一个数据库表
class Account(Base):
    # 数据表名
    __tablename__ = 'account'
    # 数据表属性定义
    username = Column(String(32), nullable=False, primary_key=True)
    password = Column(String(256), nullable=False)
    email = Column(String(32), nullable=False, unique=True)
    phone = Column(String(32), nullable=False)
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


class Device(Base):
    # 数据表名
    __tablename__ = 'device'
    # 数据表属性定义
    device_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    device_name = Column(String(50), nullable=False)
    device_type = Column(String(20), nullable=False)
    creator = Column(String(20), nullable=False)
    online = Column(Integer, nullable=False)
    creation_date = Column(DateTime, nullable=False)
    last_update_date = Column(DateTime, nullable=False)
    description = Column(String(100), nullable=True)
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


class Message(Base):
    # 数据表名
    __tablename__ = 'message'
    # 数据表属性定义
    message_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    device_id = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    alert = Column(Integer, nullable=False)
    info = Column(String(200), nullable=False)
    latitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
    value = Column(Integer, nullable=False)
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


try:
    database_url = "mysql+pymysql://iot:iot@127.0.0.1:3306/iot_backend"
    engine = create_engine(database_url, echo=True)
        
    # 检查表的存在性，如果不存在的话会执行表的创建工作
    Base.metadata.create_all(bind=engine)
    # 创建缓存对象
    Session = sessionmaker(bind=engine)
    print("mysql use port 3306")
except:
    time.sleep(5)
    database_url = "mysql+pymysql://iot:iot@127.0.0.1:3306/iot_backend"
    engine = create_engine(database_url, echo=True)
        
    # 检查表的存在性，如果不存在的话会执行表的创建工作
    Base.metadata.create_all(bind=engine)
    # 创建缓存对象
    Session = sessionmaker(bind=engine)
    print("mysql use port 3306")


if __name__ == '__main__':

    session = Session()
    devices = session.query(Device).all()
    for device in devices:
        print(device.show_info())
    session.close()
