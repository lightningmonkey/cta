from datetime import date
from get_weather_data import SingleWeatherDataPoint

class SingleStationDataPoint(object):        
    def __init__(self, raw_string):
        #column values
        self.station_id_col = 0
        self.station_name_col = 1
        self.date_col = 2
        self.day_type_col = 3
        self.rides_col = 4
        #data values
        self.station_id = 0
        self.station_name = ''
        self.date = date.fromtimestamp(0)
        self.type = ''
        self.rides = 0
        self.weather_data = SingleWeatherDataPoint('')
        self.parse_string(raw_string)
    
    def parse_string(self, raw_string):
        parsed = raw_string.split(',')
        self.station_id = int(parsed[self.station_id_col])
        self.station_name = parsed[self.station_name_col]
        parse_date_string = parsed[self.date_col].split('/')
        self.date = date(int(parse_date_string[2]), int(parse_date_string[0]), int(parse_date_string[1]))
        self.type = parsed[self.day_type_col]
        self.rides = int(parsed[self.rides_col])
        
    def __repr__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}".format(self.station_id, self.station_name, self.date, self.type, self.rides, self.weather_data)
    
    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}".format(self.station_id, self.station_name, self.date, self.type, self.rides, self.weather_data)
        
class GetCTADataParser(object):
    def __init__(self, file_name, weather):
        self.station_data_map = {}
        self.weather_map = weather
        self.run(file_name)
    
    def combine_weather_and_add(self, data_point):
        data_point.weather_data = self.weather_map[str(data_point.date)]
        if not self.station_data_map.has_key(data_point.station_name) :
                self.station_data_map[data_point.station_name] = []    
        self.station_data_map[data_point.station_name].append(data_point)
    
    def run(self, file_name):
        cur_file = open(file_name, 'r')
        for line in cur_file:
            line = line.strip()
            if 'station_id,stationname,date,daytype,rides' in line:
                continue
            data_point = SingleStationDataPoint(line)
            if data_point.type != 'W' or data_point.rides < 10:
                continue
            self.combine_weather_and_add(data_point)
        cur_file.close()
        print("Processed {0} stations", len(self.station_data_map.keys()))