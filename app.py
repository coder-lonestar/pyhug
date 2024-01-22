# import hug
from flask import Flask, send_from_directory, request
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


@app.route("/", methods=["GET"])
def greet():
    """Greets user"""
    name = request.args.get("name", default="dummy", type=str)
    key = request.args.get("key", default="fake", type=str)
    if authenticated(key):
        return {"message": "Hello {0}. Have a nice day!".format(name)}
    return {
        "message": "Unauthorized",
    }


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=80)
    app.run()
