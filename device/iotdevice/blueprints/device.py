from flask import Blueprint, jsonify, request

import iotdevice.db.service as s

device = Blueprint('device', __name__, url_prefix='/api/device_api')


@device.route('/createDevice', methods=('POST',))
def createDevice():
    device_name = request.json['device_name']
    device_type = request.json['device_type']
    creator = request.json['creator']
    online = request.json['online']
    creation_date = request.json['creation_date']
    description = request.json['description']
    retcode, message, payload = s.createDevice(device_name, device_type, creator, online, creation_date, description)
    
    if retcode:
        return jsonify({'device_id': payload, 'message': message, 'signal': 'success'}), 200
    else:
        return jsonify({'message': message, 'signal': 'fail'}), 201


@device.route('/deleteDevice', methods=('POST',))
def deleteDevice():
    device_id = request.json['device_id']
    retcode, message, payload = s.deleteDevice(int(device_id))
    
    if retcode:
        return jsonify({'message': message, 'signal': 'success'}), 200
    else:
        return jsonify({'message': message, 'signal': 'fail'}), 201


@device.route('/modifyDevice', methods=('POST',))
def modifyDevice():
    device_id = request.json['device_id']
    device_name = request.json['device_name']
    device_type = request.json['device_type']
    online = request.json['online']
    last_update_date = request.json['last_update_date']
    description = request.json['description']
    retcode, message, payload = s.modifyDevice(int(device_id), device_name, device_type, online, last_update_date, description)
    
    if retcode:
        return jsonify({'message': message, 'signal': 'success'}), 200
    else:
        return jsonify({'message': message, 'signal': 'fail'}), 201


@device.route('/getTypeDevice', methods=('POST',))
def getTypeDevice():
    device_type = request.json['device_type']
    retcode, message, payload = s.getTypeDevice(device_type)
    
    if retcode:
        return jsonify({'devices': payload, 'message': message, 'signal': 'success'}), 200
    else:
        return jsonify({'message': message, 'signal': 'fail'}), 201


@device.route('/getDefinedDevice', methods=('POST',))
def getDefinedDevice():
    device_id = request.json['device_id']
    device_name = request.json['device_name']
    device_type = request.json['device_type']
    retcode, message, payload = s.getDefinedDevice(device_id, device_name, device_type)
    
    if retcode:
        return jsonify({'devices': payload, 'message': message, 'signal': 'success'}), 200
    else:
        return jsonify({'message': message, 'signal': 'fail'}), 201
