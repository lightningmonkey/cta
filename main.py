from cta_data import CTA, CTAData
from weather_underground_data import WeatherUnderground, WeatherData
import datetime

if __name__=='__main__':
    cta = CTA()
    cta_data = CTAData()
    weather = WeatherUnderground()
    weather_data = WeatherData()
    for cur_day in range(1, 5):
        d = datetime.datetime(year=2010, month=01, day=cur_day)
        print("current date:{0}".format(d))
        cta.run(d)
        weather.run(d)
        print("===========")

#from get_cta_data import GetCTADataParser
#from get_weather_data import GetWeatherDataParser
#import pprint
#from stats import Stats

#if __name__=='__main__':
#    weather_data = GetWeatherDataParser(r'C:\Users\brian\Desktop\data\60657_weather.csv')
#    cta_data = GetCTADataParser(r'C:\Users\brian\Desktop\data\ridership.csv', weather_data.weather_data_map)
#    station_list = cta_data.station_data_map['Jackson/State']
#    stat = Stats(station_list)
#    pprint.pprint(data.station_data['Belmont-North Main'])
    #print("num: {0}".format(len(data.station_data['Southport'])))

