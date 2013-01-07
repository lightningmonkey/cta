from datetime import date

class SingleWeatherDataPoint(object):
    def __init__(self, raw_string):
        #col 
        self.date_col = 0
        self.max_temp_col = 1
        self.mean_temp_col = 2
        self.min_temp_col = 3
        self.max_gust_col = 18
        self.precip_col = 19
        self.event_col = 21
        #data
        self.date = date.today()
        self.max_temp = 0
        self.min_temp = 0
        self.mean_temp = 0
        self.max_gust = 0
        self.precip = 0
        self.events = []
        if raw_string != '':
            self.parse_string(raw_string)
    
    def parse_string(self, raw_string):
        parsed = raw_string.split(',')
        self.max_temp = int(parsed[self.max_temp_col])
        self.mean_temp = int(parsed[self.mean_temp_col])
        self.min_temp = int(parsed[self.min_temp_col])
        if parsed[self.max_gust_col] != '':
            self.max_gust = int(parsed[self.max_gust_col])
        else:
            self.max_gust = 0
        if(parsed[self.precip_col] == 'T'):
            self.precip = 0
        else:
            self.precip = float(parsed[self.precip_col])
        parse_date_string = parsed[self.date_col].split('-')
        self.date = date(int(parse_date_string[0]), int(parse_date_string[1]), int(parse_date_string[2]))
        self.events = parsed[self.event_col].split('-')
        
    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.date, self.mean_temp, self.precip, self.events)
    
    def __repr__(self):
        return "{0}, {1}, {2}, {3}".format(self.date, self.mean_temp, self.precip, self.events)
    
class GetWeatherDataParser(object):
    def __init__(self, file_name):
        self.weather_data_map = {}
        self.run(file_name)
        
    def run(self, file_name):
        f = open(file_name, 'r')
        for line in f:
            line = line.strip()
            if 'CST,Max TemperatureF,Mean TemperatureF,' in line:
                continue
            data_point = SingleWeatherDataPoint(line)
            self.weather_data_map[str(data_point.date)] = data_point
        f.close()