import urllib2
import json
import datetime


class CTAData(object):
    def __init__(self):
        self.station = ""
        self.rides = 0
        self.daytype = ""

    def __str__(self):
        return "rides:{0} station:{1} type:{2}".format(self.rides, self.station, self.daytype)

    def __repr__(self):
        return "rides:{0} station:{1} type:{2}".format(self.rides, self.station, self.daytype)

class CTA(object):
    def run(self, date):
        f = urllib2.urlopen('http://data.cityofchicago.org/resource/5neh-572f.json?station_id=41320&date={0}'.format(date.strftime("%m/%d/%Y")))
        json_string = f.read()
        parsed_json = json.loads(json_string)
        cta_data = CTAData()
        cta_data.station = parsed_json[0][u'stationname']
        cta_data.rides = parsed_json[0][u'rides']
        cta_data.daytype = parsed_json[0][u'daytype']
        print cta_data

if __name__=='__main__':
    d = datetime.datetime(year=2013, month=05, day=10)
    c = CTA()
    c.run(d)