=================
python-smartprice
=================

A simple scraping-based python library for MySmartPrice - price comparison site.

Introduction
------------

MySmartPrice_ is a platform which provided best seller price across a wide array of categories that include Mobiles, Electronics, Computers, Fashion and Lifestyle, Cameras, Books, Appliances and Personal Care.

Prerequisites
-------------
- Requests
- BeautifulSoup 4
- Python 2.7+

Quickstart
----------

.. code-block:: python

  >>> from pysmartprice.base import SmartPrice
  >>> smartprice = SmartPrice()
  
  >>> len(smartprice.samsung_mobiles)
  Out[5]: 142
  
  >>> smartprice.samsung_mobiles
  Out[6]: [<pysmartprice.results.SmartPriceResult at 0x10df46f90>,
   <pysmartprice.results.SmartPriceResult at 0x10df46fd0>,
   <pysmartprice.results.SmartPriceResult at 0x10df50050>,
   <pysmartprice.results.SmartPriceResult at 0x10df50090>,
   <pysmartprice.results.SmartPriceResult at 0x10df500d0>,
   <pysmartprice.results.SmartPriceResult at 0x10df50110>,
   <pysmartprice.results.SmartPriceResult at 0x10df50150>,
   <pysmartprice.results.SmartPriceResult at 0x10df50190>]
  
  >>> samsung_mobile = smartprice.samsung_mobiles[0]
  
  >>> samsung_mobile.title
  Out[7]: u'Samsung Galaxy J7'
  
  >>> samsung_mobile.best_price
  Out[8]: '14,299'
  
  >>> samsung_mobile.__dict__
  Out[9]: 
  {
    'best_price': u'14,299',
    'img': 'http://c0028545.cdn1.cloudfiles.rackspacecloud.com/7178-7-thumb.jpg',
    'product_id': '7178',
    'title': u'Samsung Galaxy J7',
    'url': 'http://www.mysmartprice.com/mobile/samsung-galaxy-j7-msp7178'
  }



Supported attributes
--------------------

:mobiles: Get best prices for ALL mobiles
:samsung_mobiles: Get best prices for all Samsung mobiles
:nokia_mobiles: Get best prices for all Nokia mobiles
:micromax_mobiles: Get best prices for all Micromax mobiles
:iphones: Get best prices for all IPhones
:htc_mobiles: Get best prices for all HTC mobiles


.. _MySmartPrice: http://www.mysmartprice.com/
