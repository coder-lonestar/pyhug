# import hug
from flask import Flask
import os
import base64
import logging

app = Flask(__name__)


def authenticated(key):
    salt = base64.b64decode(str.encode(os.environ["PYHUG_SALT"].strip('"'))).decode()
    password = base64.b64encode(str.encode(salt + key.strip('"'), "utf-8")).decode()
    matching_hash = os.environ["PYHUG_HASH"].strip('"')
    if password == matching_hash:
        return True
    return False


@app.route("/")
def greet(name: str, key: str = "fake"):
    """Greets user"""
    if authenticated(key):
        return {"message": "Hello {0}. Have a nice day!".format(name)}
    return {
        "message": "Unauthorized",
    }
