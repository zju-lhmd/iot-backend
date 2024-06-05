from flask import Blueprint, jsonify, request

import iotmessage.db.service as s

message = Blueprint('message', __name__, url_prefix='/api/iotmessage_api')

@message.route('/uploadMessage', methods=('POST',))
def uploadMessage():
    device_id = request.json['device_id']
    timestamp = request.json['timestamp']
    alert = request.json['alert']
    info = request.json['info']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    value = request.json['value']
    retcode, message, payload = s.uploadMessage(device_id, timestamp, alert, info, latitude, longitude, value)
    
    if retcode:
        return jsonify({'message_id': payload, 'message': message, 'signal': 'success'}), 200
    else:
        return jsonify({'message': message, 'signal': 'fail'}), 201


@message.route('/getMessage', methods=('POST',))
def getMessage():
    device_id = request.json['device_id']
    retcode, message, payload = s.getMessage(device_id)
    
    if retcode:
        return jsonify({'messages': payload, 'message': message, 'signal': 'success'}), 200
    else:
        return jsonify({'message': message, 'signal': 'fail'}), 201
