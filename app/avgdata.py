from app.scrap.wunderground import *
from app.scrap.io import *
from geopy import Nominatim


class AvgData():
    """Class for calculating average data, wu_key and io_key
    , are for api keys for forecastio and wunderground"""

    def __init__(self, city_name, wu_key, io_key, offset):
        self.geolocator = Nominatim()
        self.city_name = self.geolocator.geocode(city_name)
        self.wu_key = wu_key
        self.io_key = io_key
        self.offset = offset

    def get_lat_long(self):
        lat = self.city_name.latitude
        long = self.city_name.longitude
        loc_data = [lat, long]
        return loc_data

    def temperature(self):
        lat = self.get_lat_long()[0]
        lng = self.get_lat_long()[1]
        wu_data = ScrapWu(self.get_lat_long()[0], self.get_lat_long()[
                          1], self.offset, self.wu_key).get_temperature()
        io_data = ScrapIO(self.get_lat_long()[0], self.get_lat_long()[
                          1], self.offset, self.io_key).get_avg_temperature()
        avg_temperature = int(wu_data + io_data) / 2
        return avg_temperature

    def wind(self):
        """scraps wind from wunderground and forecast
        io and returns average daily in KpH"""
        wu_data = ScrapWu(self.get_lat_long()[0], self.get_lat_long()[
                          1], self.offset, self.wu_key).get_wind()
        io_data = ScrapIO(self.get_lat_long()[0], self.get_lat_long()[
                          1], self.offset, self.io_key).get_avg_wind()
        avg_wind = int(wu_data + io_data) / 2
        return avg_wind

    def time(self):
        io_data = ScrapIO(self.get_lat_long()[0], self.get_lat_long()[
                          1], self.offset, self.io_key).get_time()
        return io_data
