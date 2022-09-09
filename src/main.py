import os

from flask import Flask, request
import pyassimp
import urllib.request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/trigger/storage-stl-create", methods = ['POST'])
def create_object():
    print('link: {0}'.format(request.get_json()["StorageObjectData"]["selfLink"]))
    #urllib.request.urlretrieve(
        #'https://storage.googleapis.com/orobot-stls/1612589717209-battery_holder_v7.stl',
        #"orobot-stls/1612589717209-battery_holder_v7.stl")
    #scene = pyassimp.load("orobot-stls/1612589717209-battery_holder_v7.stl")
    print("scene")
    #pyassimp.export(scene, "obj-output/1612589717209-battery_holder_v7.obj", "obj")
    return "Object created."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3005)))
