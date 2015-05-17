import os
from sys import stderr, exit

from flask import Flask
from flask.ext import restful
import geoip2.database


# Create the application
app = Flask(__name__)
app.debug = True if os.getenv('IPL_DEBUG') == "True" else False
api = restful.Api(app)

# Try to create a database reader
try:
    db = geoip2.database.Reader(os.getenv('IPL_PATH_TO_GEOIP_DB'))
except TypeError:
    stderr.write('Could not find MaxMind database\n')
    exit(1)

# Maximum length of the string after "/ips"
max_request_length = os.getenv('IPL_MAX_IP_LIST_LENGTH', 1000)

from . import routes
