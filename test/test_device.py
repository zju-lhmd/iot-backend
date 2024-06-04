import pytest
from datetime import datetime
from iotdevice import create_app
from iotdevice.db import db


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
def device():
    return {
        'device_id': 1,
        'device_name': 'phone',
        'device_type': 'mobile',
        'creator': 'zhangsan',
        'online': 1,
        'creation_date': '2024-05-15',
        'description': 'my iphone'
    }


def test_createDevice(client, device):
    create_form = {
        'device_id': device['device_id'],
        'device_name': device['device_name'],
        'device_type': device['device_type'],
        'creator': device['creator'],
        'online': device['online'],
        'creation_date': device['creation_date'],
        'description': device['description']
    }
    
    # 创建设备
    response = client.post('/api/createDevice', json=create_form)
    assert response.json['signal'] == 'success'
    
    # 重复创建（device_name & device_type & creator 重复）
    response = client.post('/api/createDevice', json=create_form)
    assert response.json['signal'] == 'fail'


def test_modifyDevice(client, device):
    # 首先创建设备
    create_form = {
        'device_id': device['device_id'],
        'device_name': device['device_name'],
        'device_type': device['device_type'],
        'creator': device['creator'],
        'online': device['online'],
        'creation_date': device['creation_date'],
        'description': device['description']
    }
    client.post('/api/createDevice', json=create_form)
    
    modify_form = {
        'device_id': 1,  # 假设设备 ID 为 1
        'device_name': 'fan',
        'device_type': 'furniture',
        'online': 1,
        'last_update_date': '2024-05-16',
        'description': 'my fan'
    }
    
    response = client.post('/api/modifyDevice', json=modify_form)
    assert response.json['signal'] == 'success'


def test_getTypeDevice(client, device):
    query_form = {
        'device_type': 'furniture'
    }
    
    response = client.post('/api/getTypeDevice', json=query_form)
    assert response.json['signal'] == 'success'


def test_getDefinedDevice(client, device):
    query_form = {
        'device_id': 1,
        'device_name': 'fan',
        'device_type': 'furniture',
    }
    
    response = client.post('/api/getDefinedDevice', json=query_form)
    assert response.json['signal'] == 'success'


def test_deleteDevice(client, device):
    # 首先创建设备
    create_form = {
        'device_name': device['device_name'],
        'device_type': device['device_type'],
        'creator': device['creator'],
        'online': 1,
        'creation_date': device['creation_date'],
        'description': device['description']
    }
    client.post('/api/createDevice', json=create_form)
    
    delete_form = {
        'device_id': 1,  # 假设设备 ID 为 1
    }
    
    response = client.post('/api/deleteDevice', json=delete_form)
    assert response.json['signal'] == 'success'
