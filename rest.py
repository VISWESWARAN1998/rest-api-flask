# SWAMI KARUPPASWAMI THUNNAI

from flask import Flask
from flask_restful import Api
# Auth related resources
from auth.signup import SignUp
from auth.login import Login
# Token validator
from auth.helper import rest_token


app = Flask(__name__)
api = Api(app=app)
api.add_resource(SignUp, "/signup")
api.add_resource(Login, "/login")


@app.route("/token_test")
@rest_token
def test():
    return "Token works!"


if __name__ == "__main__":
    app.run(debug=False)
