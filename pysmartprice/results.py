import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'jsonable'):
            return obj.dumptojson
        else:
            return json.JSONEncoder.default(self, obj)


class SmartPriceBase(object):
    def __init__(self, params):
        self.__dict__.update(params)

    def jsonable(self):
        return self.__dict__

    @property
    def dumptojson(self):
        return json.loads(
            json.dumps(
                self.jsonable(),
                cls=ComplexEncoder,
                # sort_keys=True,
                indent=4,
                separators=(',', ': '))
            )


class SmartPriceResult(SmartPriceBase):
    pass


class SmartPriceSeller(SmartPriceBase):
    pass
