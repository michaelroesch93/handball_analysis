from flask import Flask, jsonify, request
import sqlite3
from player_api import *

app = Flask(__name__)


@app.route("/")

def index():
    return "Hello World!"

@app.route("/player", methods = ["POST", "GET"])

def player():
    return player_api(request)

app.run(host="0.0.0.0", port=80, debug=True)

