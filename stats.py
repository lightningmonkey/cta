from numpy import *
from get_cta_data import SingleStationDataPoint

class StatDataPoint(object):
    def __init__(self, min, max, mean, std, title):
        self.min = min
        self.max = max
        self.mean = mean
        self.std = std
        self.title = title
        print('{0} min: {1} max: {2} mean: {3} std: {4} percent: {5}'.format(title, min, max, mean, std, std/mean))

class Stats(object):
    def __init__(self, stations):
        self.station_list = stations
        self.run()

    def get_stats(self, all_list, title):
        arr = array(all_list)
        min = arr.min()
        max = arr.max()   
        mean = average(arr)  
        std = arr.std()
        return StatDataPoint(min, max, mean, std, title)

    def weekday_data(self):
        total_rides = []
        snow_rides = []
        rain_rides = []
        nice_rides = []
        for cur in self.station_list:
            total_rides.append(cur.rides)
            if(cur.weather_data.events.count('Snow') != 0):
                snow_rides.append(cur.rides)
            if(cur.weather_data.events.count('Rain') != 0 or cur.weather_data.events.count('Thunderstorm') != 0):
                rain_rides.append(cur.rides)
            if(cur.weather_data.events.count('Rain') == 0 and cur.weather_data.events.count('Thunderstorm') == 0 and cur.weather_data.events.count('Snow') == 0):
                nice_rides.append(cur.rides)
        total = self.get_stats(total_rides, 'total')
        snow = self.get_stats(snow_rides, 'snow')
        rain = self.get_stats(rain_rides, 'rain')
        nice = self.get_stats(nice_rides, 'nice')
        dif = abs(snow.mean-nice.mean)
        print('snow vs nice dif: {0} percent: {1}'.format(dif, dif/nice.mean))
        
        
    def run(self):
        self.weekday_data()