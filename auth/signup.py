# SWAMI KARUPPASWAMI THUNNAI

from flask import request, jsonify
from flask_restful import Resource
from auth.helper import hash_password
from database.get_connection import get_connection
from rest_exception import RESTException


class SignUp(Resource):

    def post(self):
        email = request.json["email"]
        name = request.json["name"]
        password = request.json["pass"]
        password = hash_password(password=password)
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select id from client_credential where email=%s limit 1", (email, ))
            if cursor.fetchone():
                return RESTException.raise_exception(RESTException.EMAIL_EXISTS)
            cursor.execute("insert into client_credential value(null, %s, %s, %s, 0)", (email, password, name))
            connection.commit()
            return jsonify({
                "message": "Account has been created!"
            })
        finally:
            cursor.close()
            connection.close()
