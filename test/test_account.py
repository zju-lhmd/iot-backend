import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
pkg_dir = os.path.join(cur_dir, '../auth')
sys.path.append(pkg_dir)

import pytest

from iotauth import create_app
from iotauth.db import db


@pytest.fixture(scope='module')
def app():
    # app = create_app('local_test')
    app = create_app('remote_test')
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def account():
    return {
        'userName': 'test-user',
        'password': '123456',
        'emailAddress': 'abc@xyz.com',
        'phoneNo': '123-456-789'
    }


def test_register(client, account):
    # 注册
    response = client.post('/api/register', json=account)
    assert response.json['state'] == 1
    # 重复注册
    response = client.post('/api/register', json=account)
    assert response.json['state'] == 0


def test_login(client, account):
    login_form = {
        'userName': account['userName'],
        'password': account['password']
    }

    # 登录
    response = client.post('/api/login', json=login_form)
    assert response.json['state'] == 1

    login_form['password'] = '456789'
    # 错误密码
    response = client.post('/api/login', json=login_form)
    assert response.json['state'] == 0


def test_chgpassword(client, account):
    chg_password_form = {
        'userName': account['userName'],
        'oldPassword': account['password'],
        'newPassword': '456789'
    }

    # 修改密码
    response = client.post('/api/updatePassword', json=chg_password_form)
    assert response.json['state'] == 1

    # 原密码错误
    response = client.post('/api/updatePassword', json=chg_password_form)
    assert response.json['state'] == 0
