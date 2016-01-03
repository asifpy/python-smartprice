from pysmartprice.price_parser import PriceListParser
from pysmartprice.constants import SMARTPRICE_ATTRS


class SmartPrice(object):

    def parser_results(self, product):
        parser = PriceListParser(product)
        return parser.price_results

    def __getattr__(self, attr):
        if attr not in SMARTPRICE_ATTRS:
            msg = '{} object has no attribute {}'
            raise AttributeError(msg.format(self.__class__.__name__, attr))

        setattr(self, attr, self.parser_results(SMARTPRICE_ATTRS[attr]))
        return getattr(self, attr)
