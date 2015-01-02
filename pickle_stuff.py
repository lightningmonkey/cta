import pickle
from weather_underground_data import WeatherData
import pprint

class PickleStuff(object):
    def __init__(self):
        self.files = ["jan_2009", "mar_2009", "feb_2009", "jun_2009", "jan_2010", "jun_2010", "mar_2010", "feb_2010"]
        #self.files = ["jan_2009"]

    def run(self, data):
        for file_str in self.files:
            f = open(file_str, "r")
            cur_data = pickle.load(f)
            data.extend(cur_data)

if __name__=='__main__':
    p = PickleStuff()
    data = []
    p.run(data)
    pprint.pprint(data)