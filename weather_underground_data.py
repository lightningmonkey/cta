import urllib2
import json
import datetime

class WeatherData(object):
    def __init__(self):
        self.temp = 0
        self.rain_fall = 0
        self.snow_depth = 0
        self.snow_fall = 0
        self.rain = False
        self.snow = False

    def __str__(self):
        return "temp:{0} rain:{1} rain_fall:{2} snow:{3} snow_depth:{4} snow_fall:{5}".format(self.temp, self.rain,
                                                                                              self.rain_fall, self.snow,
                                                                                              self.snow_depth, self.snow_fall)

    def __repr__(self):
        return "temp:{0} rain:{1} rain_fall:{2} snow:{3} snow_depth:{4} snow_fall:{5}".format(self.temp, self.rain,
                                                                                              self.rain_fall, self.snow,
                                                                                              self.snow_depth, self.snow_fall)

class WeatherUnderground(object):
    def __init__(self):
        self.api_url = "http://api.wunderground.com/api/bc2ea8943e663384/history_{0}/q/IL/Chicago.json"

    def get_val(self, input):
        try:
            output = float(input)
        except ValueError:
            output = -1
        return output

    def run(self, search_day):
        cur_search = self.api_url.format(search_day.strftime("%Y%m%d"))
        f = urllib2.urlopen(cur_search)

        json_string = f.read()
        parsed_json = json.loads(json_string)
        weather_data = WeatherData()

        weather_data.temp = self.get_val(parsed_json[u'history'][u'dailysummary'][0][u'meantempi'])
        weather_data.rain_fall = self.get_val(parsed_json[u'history'][u'dailysummary'][0][u'precipi'])
        weather_data.snow_depth = self.get_val(parsed_json[u'history'][u'dailysummary'][0][u'snowdepthi'])
        weather_data.snow_fall = self.get_val(parsed_json[u'history'][u'dailysummary'][0][u'snowfalli'])
        weather_data.rain = True if parsed_json[u'history'][u'dailysummary'][0][u'rain'] == "1" else False
        weather_data.snow = True if parsed_json[u'history'][u'dailysummary'][0][u'snow'] == "1" else False

        print weather_data
        f.close()

if __name__=='__main__':
    w = WeatherUnderground()
    d = datetime.datetime(year=2010, month=01, day=02)

    w.run(d)
    #for x in range(1,30):
    #    w.run(2014, 01, x)