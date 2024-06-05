from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

from .db import db
from .device import Device
from message.iotmessage.db.service import deleteMessages


def createDevice(device_name, device_type, creator, online, creation_date, description):
    try:
        device = Device(device_name=device_name, device_type=device_type, creator=creator, online=online, 
                        creation_date=creation_date, description=description)
        db.session.add(device)
        db.session.commit()
        device_id = str(device.device_id).zfill(5)
        return True, 'Create successfully', device_id
    
    except IntegrityError as e:
        db.session.rollback()
        print(e)
        duplicate_key = str(e).split('\'')[1]
        return False, f'{duplicate_key} already exists', None
    
    except Exception as e:
        db.session.rollback()
        print(e)
        return False, str(e), None


def deleteDevice(device_id):
    try:
        device = Device.query.get(device_id)
        if not device:
            return False, 'Device not found', None
        
        db.session.delete(device)
        db.session.commit()
        
        # 将iotmessage表中对应设备的消息也删除
        deleteMessages(device_id)
        
        return True, 'Delete successfully', None
        
    except Exception as e:
        db.session.rollback()
        print(e)
        return False, str(e), None


def modifyDevice(device_id, device_name=None, device_type=None, online=None, last_update_date=None, description=None):
    try:
        device = Device.query.get(device_id)
        if not device:
            return False, 'Device not found', device_id
        
        if device_name is not None:
            device.device_name = device_name
        if device_type is not None:
            device.device_type = device_type
        if online is not None:
            device.online = online
        if last_update_date is not None:
            device.last_update_date = last_update_date
        if description is not None:
            device.description = description
        
        db.session.commit()
        return True, 'Modify successfully', None
    
    except Exception as e:
        db.session.rollback()
        print(e)
        return False, str(e), None


def getTypeDevice(device_type):
    try:
        devices = Device.query.filter_by(device_type=device_type).all()
        
        device_list = []
        for device in devices:
            device_data = {
                'device_id': device.device_id,
                'device_name': device.device_name,
		'device_type': device.device_type,
                'creator': device.creator,
                'online': device.online,
                'creation_date': device.creation_date,
                'last_update_date': device.last_update_date,
                'description': device.description
            }
            device_list.append(device_data)
            
        return True, 'GetTypeDevice successfully', device_list
    
    except Exception as e:
        print(e)
        return False, str(e), None


def getDefinedDevice(device_id=None, device_name=None, device_type=None):
    try:
        query = Device.query
        if device_id is not None:
            query = query.filter_by(device_id=device_id)
        if device_name is not None:
            query = query.filter_by(device_name=device_name)
        if device_type is not None:
            query = query.filter_by(device_type=device_type)
        devices = query.all()
        
        device_list = []
        for device in devices:
            device_data = {
                'device_id': device.device_id,
                'device_name': device.device_name,
		'device_type': device.device_type,
                'creator': device.creator,
                'online': device.online,
                'creation_date': device.creation_date,
                'last_update_date': device.last_update_date,
                'description': device.description
            }
            device_list.append(device_data)
        
        return True, 'GetDefinedDevice successfully', device_list
    
    except Exception as e:
        print(e)
        return False, str(e), None
