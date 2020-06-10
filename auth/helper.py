# SWAMI KARUPPASWAMI THUNNAI

import time
import hashlib
import bcrypt
import jwt
from functools import wraps
from flask import request
from database.get_connection import get_connection
from rest_exception import RESTException


class RESTSecret:
    user_secret = "restSecret7894$#IND"


def hash_password(password):
    sha512 = hashlib.sha512(password.encode("utf8")).hexdigest()
    hashed_password = bcrypt.hashpw(sha512.encode("utf8"), bcrypt.gensalt())
    return hashed_password


def verify_password(password, password_hash):
    sha512 = hashlib.sha512(password.encode("utf8")).hexdigest()
    if bcrypt.checkpw(sha512.encode("utf8"), password_hash.encode("utf8")):
        return True
    return False


def generate_token(user_id, password_hash):
    payload = {
        "user_id": user_id,
        "expiry": time.time() + 259200
    }
    encoded_payload = jwt.encode(payload, password_hash + RESTSecret.user_secret)
    return encoded_payload.decode("utf8")


def rest_token(_function):

    @wraps(_function)
    def wrapper_function(*args, **kwargs):
        try:
            api_key = request.headers["x-access-token"]
        except KeyError:
            return RESTException.raise_exception(RESTException.TOKEN_MISSING)
        try:
            decoded_token = jwt.decode(api_key, verify=False)
            expiry = decoded_token["expiry"]
            user_id = decoded_token["user_id"]
        except jwt.DecodeError:
            return RESTException.raise_exception(RESTException.INVALID_TOKEN)
        except KeyError:
            return RESTException.raise_exception(RESTException.INVALID_TOKEN)
        if time.time() > expiry:
            return RESTException.raise_exception(RESTException.TOKEN_EXPIRED)
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select password from client_credential where id=%s limit 1", (user_id, ))
            result = cursor.fetchone()
            if result is None:
                return RESTException.raise_exception(RESTException.INCORRECT_PASSWORD)
            password_hash = result["password"]
            try:
                jwt.decode(api_key, password_hash + RESTSecret.user_secret)
            except jwt.DecodeError:
                return RESTException.raise_exception(RESTException.INVALID_TOKEN)
        finally:
            cursor.close()
            connection.close()
        return _function(*args, **kwargs)
    return wrapper_function
