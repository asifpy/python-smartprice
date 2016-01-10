import json


class SmartPriceResult(object):
    def __init__(self, params):
        self.__dict__.update(params)

    def dumpjson(self):
        return json.dumps(self.__dict__)
