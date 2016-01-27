from pysmartprice.abstract import(
    BaseParser,
    ParserMixin
)
from pysmartprice.helpers import scrape
from bs4 import BeautifulSoup
from pysmartprice.results import SmartPriceSeller


class PriceListParser(BaseParser, ParserMixin):
    @property
    def get_paged_url(self):
        i = self.url.find(self.mapper)
        paged_url = '{}pages/{}'.format(self.url[:i], self.url[i:])
        return paged_url


class SearchParser(BaseParser, ParserMixin):
    @property
    def get_paged_url(self):
        return self.url


# SCRAPE SELLERS
class SellerParser(object):
    def __init__(self, url, *args, **kwargs):
        self.url = url
        self.response = scrape(self.url, **kwargs)
        self.soup = BeautifulSoup(self.response, 'lxml')
        self.result = [
            SmartPriceSeller(self.get_product_attrs(item))
            for item in self.products_html
            ]

    def get_product_attrs(self, item):
        return dict(
            logo=item.find('img', {'class': 'prc-tbl__str-logo'}).get('src'),
            rating=item.find(
                'span', attrs={'class': 'rtng-bdg rtng-bdg--dark-grn'}).text,
            price=item.find(
                'span', attrs={'class': 'prc-tbl__cost-val'}).text,
            name=item.find('div', attrs={'class': 'prc-tbl__slr-name'}).text
        )

    @property
    def products_html(self):
        html = self.soup.findAll(
            'div', attrs={'class': 'prc-tbl-row__inr clearfix'})
        return html
