# SWAMI KARUPPASWAMI THUNNAI

from flask import request, jsonify
from flask_restful import Resource
from database.get_connection import get_connection
from rest_exception import RESTException
from auth.helper import verify_password, generate_token


class Login(Resource):

    def post(self):
        email = request.json["email"]
        password = request.json["pass"]
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id, password from client_credential where email=%s limit 1", (email, ))
            result = cursor.fetchone()
            if result is None:
                return RESTException.raise_exception(RESTException.DATA_NOT_PRESENT)
            if not verify_password(password, result["password"]):
                return RESTException.raise_exception(RESTException.INCORRECT_PASSWORD)
            return jsonify({
                "message": generate_token(result["id"], result["password"])
            })
        finally:
            cursor.close()
            connection.close()