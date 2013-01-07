from get_cta_data import GetCTADataParser
from get_weather_data import GetWeatherDataParser
import pprint
from stats import Stats

if __name__=='__main__':
    weather_data = GetWeatherDataParser(r'C:\Users\brian\Desktop\data\60657_weather.csv')
    cta_data = GetCTADataParser(r'C:\Users\brian\Desktop\data\ridership.csv', weather_data.weather_data_map)
    station_list = cta_data.station_data_map['Jackson/State']
    stat = Stats(station_list)
    #pprint.pprint(data.station_data['Belmont-North Main'])
    #print("num: {0}".format(len(data.station_data['Southport'])))
    