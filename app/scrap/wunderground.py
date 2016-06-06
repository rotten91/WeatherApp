from datetime import datetime, timedelta
from urllib import request
import codecs
import json
import contextlib


class ScrapWu():

    def __init__(self, lat, long, offset, api_key):
        self.latitude = lat
        self.longitude = long
        self.offset = offset
        self.api_key = api_key

    def get_time(self):
        date = datetime.now() - timedelta(days=self.offset)
        day = date.strftime('%Y%m%d')
        return str(day)

    def get_json(self):
        url_start = 'http://api.wunderground.com/api/'
        url_end = '/{0}/geolookup/history_{1}/q/{2},{3}.json'
        url = str(url_start + url_end).format(self.api_key, self.get_time(),
                                              self.latitude, self.longitude)

        with contextlib.closing(request.urlopen(url)) as u:
            json_data = request.urlopen(url)
            reader = codecs.getreader('utf-8')
            parsed_json = json.load(reader(json_data))
        return parsed_json

    def get_temperature(self):
        data = self.get_json()
        temperature = data['history']['dailysummary'][0]['meantempm']
        return int(temperature)

    def get_wind(self):
        data = self.get_json()
        wind = data['history']['dailysummary'][0]["meanwindspdm"]
        return int(wind)
#q = ScrapWu(lat, lng, 1, api_key='8aa4b38d78a0c7b3')
#print("dzisiejsza temperatura to:{}".format(q.get_temperature()))
