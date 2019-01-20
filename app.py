from flask import Flask, Response
from flask_cors import CORS
from cozify import cloud, hub
from time import sleep
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    devices = parse_cozify_resp(hub.devices(capabilities=hub.capability.TEMPERATURE))
    return Response(response=json.dumps(devices), status=200, mimetype="application/json", headers={"encoding":"utf-8"})

def parse_cozify_resp(cresp):
    parsed = {}
    parsed["devices"] = []
    for id, dev in cresp.items():
        new_dev = {}
        new_dev["name"] = dev["name"]
        new_dev["id"] = id
        new_dev["temp"] = dev["state"]["temperature"]
        parsed["devices"].append(new_dev)
    return parsed