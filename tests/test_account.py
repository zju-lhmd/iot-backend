import pytest
from AuthMicroservices import create_app


@pytest.fixture(scope='module')
def app():
    app = create_app('testing')
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def account():
    return {'userName': 'test-user',
            'password': '123456',
            'emailAddress': 'abc@xyz.com',
            'phoneNo': '123-456-789'}


def test_account(client, account):
    # 尝试注册
    response = client.post('/api/register', json=account)
    assert response.json['state'] == 1
    # 重复注册
    response = client.post('/api/register', json=account)
    assert response.json['state'] == 0

    # 尝试登录
    login_form = {'userName': account['userName'], 'password': account['password']}
    response = client.post('/api/login', json=login_form)
    assert response.json['state'] == 1
    # 错误登录
    login_form['password'] = '456789'
    response = client.post('/api/login', json=login_form)
    assert response.json['state'] == 0

    # 修改密码
    chg_password_form = {'userName': account['userName'],
                         'oldPassword': account['password'],
                         'newPassword': '456789'}
    response = client.post('/api/updatePassword', json=chg_password_form)
    assert response.json['state'] == 1
    # 原密码错误
    response = client.post('/api/updatePassword', json=chg_password_form)
    assert response.json['state'] == 0
