# SWAMI KARUPPASWAMI THUNNAI

import pymysql
from sys import platform


def get_connection():
    if "linux" in platform:
        connection = pymysql.connect(
            host="127.0.0.1", user="root", password="#xoW4TOJnKz7",
            db="rest", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor
        )
    else:
        connection = pymysql.connect(
            host="127.0.0.1", user="root", password="visweswaran",
            db="rest", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor
        )
    return connection