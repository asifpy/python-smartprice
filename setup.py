import os
from setuptools import setup
import pysmartprice

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='python-smartprice',
    version=pysmartprice.VERSION,
    packages=['pysmartprice'],
    include_package_data=True,
    license='BSD License',
    description='A simple scraping-based python library for MySmartPrice',
    long_description=README,
    url='https://github.com/asifpy/python-smartprice',
    author='Asif Jamadar',
    author_email='saluasif@gmail.com',
    keywords=['smartprice', 'price comparision', 'scrapping'],
    install_requires=[
        'requests>=2.5.3',
        'beautifulsoup4>4.4.0',
        'pytest>=2.8.5',
    ],
)
