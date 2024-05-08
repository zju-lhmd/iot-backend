from sqlalchemy.exc import IntegrityError

from .db import db
from .account import Account


def addAccount(username, password, email, phone):
    try:
        _account = Account(username, password, email, phone)
        db.session.add(_account)
        db.session.commit()
        return True, None, None
    except IntegrityError as e:
        db.session.rollback()
        print(e)
        duplicate_key = str(e).split('\'')[1]
        return False, f'{duplicate_key} already exists', duplicate_key
    except Exception as e:
        db.session.rollback()
        print(e)
        return False, str(e), None


def authAccount(username, password):
    try:
        result = db.session.query(Account).get(username)
        if result is None:
            return False, 'User not found', username
        if result.password == password:
            return True, None, None
        else:
            return False, 'Wrong password', password
    except Exception as e:
        print(e)
        return False, str(e), None


def infoAccount(username):
    try:
        result = db.session.query(Account).get(username)
        if result is None:
            return False, 'User not found', username
        return True, None, result.get()
    except Exception as e:
        print(e)
        return False, str(e), None


def chgAccountPassword(username, old_password, new_password):
    try:
        result = db.session.query(Account).get(username)
        if result is None:
            return False, 'User not found', username
        if result.password == old_password:
            result.password = new_password
            db.session.commit()
            return True, None, None
        else:
            return False, 'Wrong password', old_password
    except Exception as e:
        db.session.rollback()
        print(e)
        return False, str(e), None


def chgAccountInfo(username, email, phone):
    try:
        result = db.session.query(Account).get(username)
        if result is None:
            return False, 'User not found', username
        result.email = email
        result.phone = phone
        db.session.commit()
        return True, None, None
    except IntegrityError as e:
        db.session.rollback()
        print(e)
        duplicate_key = str(e).split('\'')[1]
        return False, f'{duplicate_key} already exists', duplicate_key
    except Exception as e:
        db.session.rollback()
        print(e)
        return False, str(e), None
