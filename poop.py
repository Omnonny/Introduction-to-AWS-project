from flask import Flask
import os
import sys
import json

proj = Flask(__name__)

@proj.route("/")
def hello():
    return "<p>Hello</p>"
    






