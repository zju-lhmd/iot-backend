import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
pkg_dir = os.path.join(cur_dir, '../message')
sys.path.append(pkg_dir)

import pytest
from datetime import datetime
from iotmessage import create_app
from iotmessage.db import db


@pytest.fixture(scope='module')
def app():
    # 创建 Flask 应用，配置为测试环境
    app = create_app('remote_test')
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def message():
    return {
        'message_id': 1,
        'device_id': 1,
        'timestamp': '2024-05-30 11:52:53',
        'alert': 0,
        'info': '111',
        'latitude': 103.55,
        'longitude': 105.33,
        'value': 40
    }


def test_uploadMessage(client, message):
    create_form = {
        'message_id': message['message_id'], 
        'device_id': message['device_id'],
        'timestamp': message['timestamp'],
        'alert': message['alert'],
        'info': message['info'],
        'latitude': message['latitude'],
        'longitude': message['longitude'],
        'value': message['value']
    }
    
    # 创建消息
    response = client.post('/api/iotmessage_api/uploadMessage', json=create_form)
    assert response.json['signal'] == 'success'
    
    # 重复创建
    response = client.post('/api/iotmessage_api/uploadMessage', json=create_form)
    assert response.json['signal'] == 'success'


def test_getMessage(client, message):
    query_form = {
        'device_id': 1
    }
    
    response = client.post('/api/iotmessage_api/getMessage', json=query_form)
    assert response.json['signal'] == 'success'
