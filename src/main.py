import os

from flask import Flask
from pyassimp import load

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/trigger/storage-stl-create")
def create_object():
    app.logger.debug('Body: %s', request.get_data())
    return "Object created."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3005)))
