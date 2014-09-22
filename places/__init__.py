from flask import Flask

from mongoengine import *

connect()

app = Flask(__name__)

from places.views import rest
