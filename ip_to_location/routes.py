from . import api
from .models import LookupRequest


api.add_resource(LookupRequest, '/ip',
                                '/ip/<string:ips>',
                                '/ips/<string:ips>')
