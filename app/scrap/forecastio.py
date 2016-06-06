from datetime import timedelta, datetime
import forecastio

lat = '52.370235'
lng = '4.903549'


class ScrapIO():

    def __init__(self, lat, long, offset, api_key):
        self.latitude = lat
        self.longitude = long
        self.offset = offset
        self.api_key = api_key

    def get_time(self):
        date = datetime.now() - timedelta(days=self.offset) + timedelta(hours=0)
        return date

    def scrap_io(self):
        forecast = fore.load_forecast(self.api_key, self.latitude, self.longitude,
                                 time=self.get_time(), units='si')
        return forecast

    def get_avg_daily(self):
        avg_data = self.scrap_io()
        avg_daily = avg_data.daily()
        avg_daily = avg_daily.data
        return avg_daily

    def get_avg_temperature(self):
        avg_data = self.get_avg_daily()
        for i in avg_data:
            avg_daily_temperature = (i.temperatureMin + i.temperatureMax)
            avg_daily_temperature = round(avg_daily_temperature / 2, 2)
        return avg_daily_temperature

    def get_avg_wind(self):
        avg_data = self.get_avg_daily()
        for i in avg_data:
            avg_daily_wind = i.windSpeed
        return avg_daily_wind

q = ScrapIO(lat, lng, 0, '15f0dcbd752adbe5bc417321d6d8f3dd')
print(q.get_time())
print(q.get_avg_daily())
print(q.get_avg_temperature())
print(q.get_avg_wind())
