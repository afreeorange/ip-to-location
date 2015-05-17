# IP to Location

An API interface to [MaxMind's free GeoIP2 database](https://www.maxmind.com/en/geolocation_landing). Here's what a sample response will look like:

![Sample response](http://i.imgur.com/OtRsR2J.png)

Installation
------------

Get the MaxMind database

	GEOLITE2_LOCATION='http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'
	wget -O - $GEOLITE2_LOCATION | gunzip - > /tmp/GeoLite2-City.mmdb

Then set an environment variable called `$IPL_PATH_TO_GEOIP_DB` to the path.

To debug, set `$IPL_DEBUG` to "True".

In a virtual environment, install the dependencies

	pip install -r requirements.txt

Fire it up

	gunicorn -b 0.0.0.0:8080 ip_to_location:app

See the `ui` folder for a simple front end to the app. Add IPs like so

	ipl.html?128.255.78.67,122.240.1.5

It looks like this:

![UI](http://i.imgur.com/4C8kCFO.png)

License
-------

[MIT](https://raw.githubusercontent.com/afreeorange/mit-license/master/LICENSE)
