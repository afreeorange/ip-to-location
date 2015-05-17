import re

from . import db
import models


def lookup(ip):
    """ Look up a single IP address in the MaxMind database
    """
    lookup = models.Lookup(ip=ip)

    # Validate the IP address
    if valid_ip(ip):
        try:
            db_data = db.city(ip)
        except Exception, e:
            lookup.data = {'error': 'Couldn\'t find address in database'}
        else:
            lookup.data = {
                'city': db_data.city.name,
                'continent': db_data.continent.name,
                'country': db_data.country.name,
                'country_code': db_data.country.iso_code,
                'host': hostname(ip)[0],
                'latitude': db_data.location.latitude,
                'longitude': db_data.location.longitude,
                'postal_code': db_data.postal.code,
                'state': db_data.subdivisions.most_specific.iso_code,
                'time_zone': db_data.location.time_zone,
            }
    else:
        lookup.data = {'error': 'I don\'t think this is a valid address'}        

    return lookup.data


def hostname(ip):
    """ Attempts a reverse lookup of the hostname.
        There does exist a GeoIP2 domain database but it's not free.
    """
    try:
        return socket.gethostbyaddr(ip)
    except Exception:
        return None, None, None


def valid_ip(ip):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return True
    else:
        return False
