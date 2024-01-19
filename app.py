import hug
import os
import base64


def authenticated(key, salt):
    salt = os.environ["PYHUG_SALT"].strip('"')
    password = base64.b64encode(str.encode(salt + key.strip('"'), "utf-8")).decode()
    matching_hash = os.environ["PYHUG_HASH"].strip('"')
    if password == matching_hash:
        return True
    return False

@hug.get("/")
@hug.local()
def greet(name: hug.types.text, key: hug.types.text = "fake", hug_timer=3):
    """Greets user"""
    if authenticated:
        return {
            "message": "Hello {0}. Have a nice day!".format(name),
            "took": float(hug_timer),
        }
    return {
        "message": "Unauthorized",
        "took": float(hug_timer),
    }

@hug.get('/data')
@hug.local()
def get_data(hug_timer=3):
    """Returns Data"""
    