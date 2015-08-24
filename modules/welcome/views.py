#!/usr/bin/python3

from bottle import route
from settings import config

@route("/app")
def index():
    return "Soy una app!!"

if config.default_module=="app":

    index = route("/")(index)

