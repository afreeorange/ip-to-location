from . import max_request_length
from .helpers import lookup
from flask import request
from flask.ext import restful


class Lookup(object):
    def __init__(self, ip=None):
        super(Lookup, self).__init__()
        self._ip = ip
        self._data = {
            self._ip: {
                'city': None,
                'continent': None,
                'country': None,
                'country_code': None,
                'host': None,
                'latitude': None,
                'longitude': None,
                'postal_code': None,
                'state': None,
                'time_zone': None,
            }
        }

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data[self._ip] = value


class LookupRequest(restful.Resource):
    def get(self, ips=None):
        if ips:
            if len(ips) > max_request_length:
                return {'error': 'I hate so much about the things that '
                                 'you choose to be'}, 400
            else:
                ips = ips.split(',')                
        else:
            ips = [request.environ['REMOTE_ADDR']]

        response = {}
        for ip in ips:
            response.update(lookup(ip))

        return response
