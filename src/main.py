import os

from flask import Flask, request
import pyassimp
import urllib.request
import json
from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import uuid

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/trigger/storage-stl-create", methods = ['POST'])
def create_object():
    jsonBody = request.get_json()
    mediaLink = jsonBody["mediaLink"]
    name = jsonBody["name"]
    filename = str(uuid.uuid4())
    tmpPathDirs = "/tmp/orobot-cloud-run/in"
    tmpPath = "{0}/{1}.stl".format(tmpPathDirs, filename);
    tmpExportPathDirs = "/tmp/orobot-cloud-run/export"
    tmpExportPath = "{0}/{1}.obj".format(tmpExportPathDirs, filename);
    if not os.path.exists(tmpPathDirs):
        os.makedirs(tmpPathDirs)
    if not os.path.exists(tmpExportPathDirs):
        os.makedirs(tmpExportPathDirs)
    print('link: {0}'.format(json.dumps(request.get_json())))
    urllib.request.urlretrieve(
        mediaLink,
        tmpPath)
    print("file downloaded")
        #"orobot-stls/1612589717209-battery_holder_v7.stl")
    scene = pyassimp.load(tmpPath)
    print("scene")
    pyassimp.export(scene, tmpExportPath, "obj")
    print("obj created")
    client = storage.Client()

    bucket = client.get_bucket('orobot-obj')
    blob = bucket.blob("{0}.obj".format(os.path.splitext(name)[0]))
    blob.upload_from_filename(tmpExportPath)
    return "Object created."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3005)))
