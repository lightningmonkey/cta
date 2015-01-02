from weather_underground_data import WeatherData
from cta_data import CTAData, CTA
from pickle_stuff import PickleStuff
import pprint
import pickle

class CombinedData(object):
    def __init__(self, weather, cta):
        self.weather_data = weather
        self.cta_data = cta

    def __str__(self):
        return "weather[{0}]\ncta[{1}]".format(self.weather_data, self.cta_data)

    def __repr__(self):
        return "weather[{0}]\ncta[{1}]".format(self.weather_data, self.cta_data)

class Combine(object):
    def __init__(self):
        p = PickleStuff()
        self.weather_data = []
        p.run(self.weather_data)
        self.combined_data = []

    def run(self):
        cta = CTA()
        for weather_data in self.weather_data:
            c = cta.run(weather_data.date)
            combined = CombinedData(weather_data, c)
            self.combined_data.append(combined)

        pprint.pprint(self.combined_data)
        f = open("combined", "w")
        pickle.dump(self.combined_data, f)
        f.close()

if __name__=='__main__':
    c = Combine()
    c.run()

