import unittest
import pytest
import requests

from pysmartprice.base import SmartPrice
from pysmartprice import constants


class TestSmartPrice(unittest.TestCase):

    def setUp(self):
        self.smartprice = SmartPrice()
        # self.generate_soupelement_tests()

    # def generate_soupelement_tests(self):
    #     """Generate test methods to check valid URLS"""
    #     for key, url in constants.URL_MAPPER.iteritems():
    #         testmethodname = 'test_fn_{0}'.format(key)
    #         testmethod = lambda self: self.assertEqual(key, key)
    #         setattr(TestSmartPrice, testmethodname, testmethod)

    def test_webexists(self):
        self.assertEqual(
            'http://www.mysmartprice.com/',
            constants.SMARTPRICE_WEB_URL
            )

    def test_validurls(self):
        for key, url in constants.URL_MAPPER.iteritems():
            complete_url = '{}{}'.format(constants.SMARTPRICE_WEB_URL, url)
            requests.get(complete_url)
