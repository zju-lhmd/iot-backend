from flask import Blueprint, jsonify, request

import AuthMicroservices.db.services as s


account = Blueprint('account', __name__, url_prefix='/api')


@account.route('/register', methods=('POST',))
def register():
    username = request.json['userName']
    password = request.json['password']
    email = request.json['emailAddress']
    phone = request.json['phoneNo']
    retcode, message, payload = s.addAccount(username, password, email, phone)

    if retcode:
        return jsonify({'state': 1, 'message': ''}), 200
    elif payload is not None:
        return jsonify({'state': 0, 'message': message}), 200
    else:
        return jsonify({'state': 0, 'message': ''}), 200


@account.route('/login', methods=('POST',))
def login():
    username = request.json['userName']
    password = request.json['password']
    retcode, message, payload = s.authAccount(username, password)

    if retcode:
        return jsonify({'state': 1, 'message': ''}), 200
    elif payload is not None:
        return jsonify({'state': 0, 'message': message}), 200
    else:
        return jsonify({'state': 0, 'message': ''}), 200


@account.route('/showInfo', methods=('POST',))
def show_info():
    username = request.json['userName']
    retcode, message, payload = s.infoAccount(username)

    if retcode:
        return jsonify({'state': 1, 'message': ''}), 200
    elif payload is not None:
        return jsonify({'state': 0, 'message': message}), 200
    else:
        return jsonify({'state': 0, 'message': ''}), 200


@account.route('/updatePassword', methods=('POST',))
def chg_password():
    username = request.json['userName']
    old_password = request.json['oldPassword']
    new_password = request.json['newPassword']
    retcode, message, payload = s.chgAccountPassword(username, old_password, new_password)

    if retcode:
        return jsonify({'state': 1, 'message': ''}), 200
    elif payload is not None:
        return jsonify({'state': 0, 'message': message}), 200
    else:
        return jsonify({'state': 0, 'message': ''}), 200


@account.route('/updateInfo', methods=('POST',))
def chg_info():
    username = request.json['userName']
    email = request.json['emailAddress']
    phone = request.json['phoneNo']
    retcode, message, payload = s.chgAccountInfo(username, email, phone)

    if retcode:
        return jsonify({'state': 1, 'message': ''}), 200
    elif payload is not None:
        return jsonify({'state': 0, 'message': message}), 200
    else:
        return jsonify({'state': 0, 'message': ''}), 200
