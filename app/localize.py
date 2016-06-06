from geopy import Nominatim

__all__ = ['Localize']


class Localize():
    'Scraps lat, long data from given city name usin geopy library'
    def __init__(self, city_name):
        self.geolocator = Nominatim()
        self.city_name = self.geolocator.geocode(city_name)

    def get_lat_long(self):
        lat = self.city_name.latitude
        long = self.city_name.longitude
        loc_data = [lat, long]
        return loc_data

