=================
python-smartprice
=================

A simple scraping-based python library for MySmartPrice - price comparison site.

Introduction
------------

MySmartPrice_ is a platform which provided best seller price across a wide array of categories that include Mobiles, Electronics, Computers, Fashion and Lifestyle, Cameras, Books, Appliances and Personal Care.


Installation
------------

``pip install python-smartprice``


Prerequisites
-------------
- Requests
- BeautifulSoup 4
- Python 2.7+

Quickstart
----------

GET PRICE LIST
--------------

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
  
  >>> samsung_mobile.dumptojson
  Out[9]: 
        '{
          "url": "http://www.mysmartprice.com/mobile/htc-desire-820-g-plus-msp7467",
          "best_price": "13,592",
          "product_id": "7467",
          "img": "http://c0028545.cdn1.cloudfiles.rackspacecloud.com/7467-7-thumb.jpg",
          "title": "\\nHTC Desire 820G Plus\\n"
        }'

SEARCH PRICE LIST
-----------------

.. code-block:: python
  
  >>> from pysmartprice.base import SmartPrice
  >>> smartprice = SmartPrice()
  
  >>> smartprice.search('SAMSUNG')
  Out[4]: [<pysmartprice.results.SmartPriceResult at 0x102b05990>,
  <pysmartprice.results.SmartPriceResult at 0x100d36850>,
  <pysmartprice.results.SmartPriceResult at 0x1024129d0>,
  <pysmartprice.results.SmartPriceResult at 0x102412b10>,
  <pysmartprice.results.SmartPriceResult at 0x102412f90>,
  <pysmartprice.results.SmartPriceResult at 0x102412fd0>,
  <pysmartprice.results.SmartPriceResult at 0x102412e10>,
  <pysmartprice.results.SmartPriceResult at 0x102412d50>,
  <pysmartprice.results.SmartPriceResult at 0x102412c50>,
  ...]
  
  In [3]: len(s.search('SAMSUNG'))
  Out[3]: 1012
  



Supported attributes
--------------------

:mobiles: Get best prices for ALL mobiles
:samsung_mobiles: Get best prices for all Samsung mobiles
:nokia_mobiles: Get best prices for all Nokia mobiles
:micromax_mobiles: Get best prices for all Micromax mobiles
:iphones: Get best prices for all IPhones
:htc_mobiles: Get best prices for all HTC mobiles


.. _MySmartPrice: http://www.mysmartprice.com/
