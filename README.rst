
|Build|_ |CodeRate|_ |pypi|_

.. |Build| image:: https://scrutinizer-ci.com/g/asifpy/python-smartprice/badges/build.png?b=master
.. _Build: https://scrutinizer-ci.com/g/asifpy/python-smartprice/

.. |CodeRate| image:: https://scrutinizer-ci.com/g/asifpy/python-smartprice/badges/quality-score.png?b=master
.. _CodeRate: https://scrutinizer-ci.com/g/asifpy/python-smartprice/

.. |pypi| image:: https://badge.fury.io/py/python-smartprice.svg
.. _pypi: https://badge.fury.io/py/python-smartprice



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

Check all the below `Supported attributes`_.

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
    {u'best_price': u'14,664',
     u'img': u'http://c0028545.cdn1.cloudfiles.rackspacecloud.com/7178-7-thumb.jpg',
     u'product_id': u'7178',
     u'title': u'\nSamsung Galaxy J7\n',
     u'url': u'http://www.mysmartprice.com/mobile/samsung-galaxy-j7-msp7178'}

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
  
  In [3]: results = s.search('SAMSUNG')
  
  In [4]: results[0].dumptojson
  Out[4]: 
    {u'best_price': u'14,664',
     u'img': u'http://c0028545.cdn1.cloudfiles.rackspacecloud.com/7178-7-thumb.jpg',
     u'product_id': u'7178',
     u'title': u'\nSamsung Galaxy J7\n',
     u'url': u'http://www.mysmartprice.com/mobile/samsung-galaxy-j7-msp7178'}
  
GET SELLERS DETAILS
-------------------

.. code-block:: python

  >> from pysmartprice.base import SmartPrice
  >> smartprice = SmartPrice()
  
  >> results = smartprice.sellers('Samsung Galaxy J2')
  >> results
  Out[4]: [<pysmartprice.results.SmartPriceResult at 0x109eca590>]
  
  In [5]: results[0].dumptojson
  Out[5]: 
    {'best_price': '8,199',
     'img': 'http://c0028545.cdn1.cloudfiles.rackspacecloud.com/7448-6-thumb.jpg',
     'product_id': '7448',
     'title': 'Samsung Galaxy J2',
     'sellers': [
        {'logo': u'http://c223968.r68.cf1.rackcdn.com/syberplace_store.png',
         'name': u'Seller:\nSyberplace',
         'price': u'8,199',
         'rating': u'5/5'},
        {'logo': u'http://c223968.r68.cf1.rackcdn.com/amazon_store.png',
         'name': u'Seller:Amazon Seller',
         'price': u'8,330',
         'rating': u'4.5/5'},
        {'logo': u'http://c223968.r68.cf1.rackcdn.com/ebay_store.png',
         'name': u'Seller:Bberry.stores',
         'price': u'8,215',
         'rating': u'5/5'},
        {'logo': u'http://c223968.r68.cf1.rackcdn.com/paytm_store.png',
         'name': u'Seller:RYAISHA RETAILS PVT LTD',
         'price': u'8,496',
         'rating': u'3.2/5'},
        {'logo': u'http://c223968.r68.cf1.rackcdn.com/indiatimes_store.png',
         'name': u'Seller:Indiatimes',
         'price': u'8,314',
         'rating': u'2.5/5'},
        {'logo': u'http://c223968.r68.cf1.rackcdn.com/flipkart_store.png',
         'name': u'Seller:WS Retail',
         'price': u'8,499',
         'rating': u'4.2/5'}],
    'url': 'http://www.mysmartprice.com/mobile/samsung-galaxy-j2-msp7448'}



Supported attributes
--------------------
Get the best prices for the below attributes

- mobiles
- samsung_mobiles
- nokia_mobiles
- micromax_mobiles
- iphones
- htc_mobiles
- tablets
- samsung_tablets
- lenovo_tablets
- micromax_tablets
- apple_ipads
- laptops
- hp_laptops
- dell_laptops
- lenovo_laptops
- sony_laptops
- toshiba_laptops
- macbooks
- samsung_laptops
- tvs
- samsung_tvs
- sony_tvs
- lg_tvs
- panasonic_tvs
- sharp_tvs


.. _MySmartPrice: http://www.mysmartprice.com/
