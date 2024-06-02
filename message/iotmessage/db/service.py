from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

from .db import db
from .message import Message


def uploadMessage(device_id, timestamp, alert, info, latitude, longitude, value):
    try:
        message = Message(device_id=device_id, timestamp=timestamp, alert=alert, info=info, 
                        latitude=latitude, longitude=longitude, value=value)
        db.session.add(message)
        db.session.commit()
        message_id = str(message.message_id).zfill(5)
        return True, 'Create successfully', message_id
    
    except IntegrityError as e:
        db.session.rollback()
        print(e)
        duplicate_key = str(e).split('\'')[1]
        return False, f'{duplicate_key} already exists', None
    
    except Exception as e:
        db.session.rollback()
        print(e)
        return False, str(e), None


def getMessage(device_id):
    try:
        messages = Message.query.filter_by(device_id=device_id).all()
        
        message_list = []
        for message in messages:
            message_data = {
                'message_id': message.message_id,
                'device_id': message.device_id,
                'timestamp': message.timestamp,
                'alert': message.alert,
                'info': message.info,
                'latitude': message.latitude,
                'longitude': message.longitude,
                'value': message.value
            }
            message_list.append(message_data)
            
        return True, 'GetMessage successfully', message_list
    
    except Exception as e:
        print(e)
        return False, str(e), None
