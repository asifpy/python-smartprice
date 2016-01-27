import json


class SmartPriceBase(object):
    def __init__(self, params):
        self.__dict__.update(params)

    @property
    def dumptojson(self):
        return json.dumps(self.__dict__)


class SmartPriceResult(SmartPriceBase):
    pass


class SmartPriceSeller(SmartPriceBase):
    pass
