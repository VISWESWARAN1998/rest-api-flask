# SWAMI KARUPPASWAMI THUNNAI

from flask import jsonify


class RESTException:

    INVALID_EMAIL = 1
    EMAIL_EXISTS = 2
    DATA_NOT_PRESENT = 4
    INCORRECT_PASSWORD = 5
    TOKEN_MISSING = 6
    INVALID_TOKEN = 7
    TOKEN_EXPIRED = 8

    EXCEPTION_DICT = {
        INVALID_EMAIL: "The phone/email number which you have entered is invalid.",
        EMAIL_EXISTS: "The phone/email number exists on our system",
        DATA_NOT_PRESENT: "The requested data is not present in the database.",
        INCORRECT_PASSWORD: "The password is incorrect!",
        TOKEN_MISSING: "The API key is missing.",
        INVALID_TOKEN: "The API key is invalid.",
        TOKEN_EXPIRED: "The API key has been expired"
    }

    @staticmethod
    def raise_exception(exception_id):
        response = jsonify(
            {
                "exception_id": exception_id,
                "message": RESTException.EXCEPTION_DICT[exception_id]
            }
        )
        response.status_code = 400
        return response
