import multiprocessing
from bs4 import BeautifulSoup

from pysmartprice.results import SmartPriceResult
from pysmartprice.helpers import scrape, scrape_helper
from pysmartprice import constants


class BaseParser(object):
    def __init__(self, mapper, **kwargs):
        self.mapper = mapper
        self.params = kwargs
        self.url = constants.URL_MAPPER[self.mapper]
        self.response = scrape(self._make_url(self.url), **kwargs)
        self.soup = BeautifulSoup(self.response, 'lxml')
        self.result = [
            SmartPriceResult(self.get_product_attrs(item))
            for item in self.products_html
            ]

    def _make_url(self, target):
        return '{}{}'.format(constants.SMARTPRICE_WEB_URL, target)

    @property
    def price_results(self):
        if self.get_page_range:
            return self.process_multiple_pages()

        return self.result


class ParserMixin(object):
    def get_product_attrs(self, item):
        return dict(
            img=item.find('img').get('src'),
            title=item.find('a', attrs={'class': 'prdct-item__name'}).text,
            url=item.find(
                'a', attrs={'class': 'prdct-item__name'}).get('href'),
            best_price=item.find(
                'span', attrs={'class': 'prdct-item__prc-val'}).text,
            product_id=item.get('data-mspid')
        )

    @property
    def products_html(self):
        html = self.soup.findAll('div', attrs={'class': 'prdct-item'})
        return html

    def process_multiple_pages(self):
        results = self.result
        first_page, last_page = self.get_page_range
        paged_url = self.get_paged_url
        page_urls = []

        for page in range(first_page+1, last_page+1):
            url = paged_url.replace('.html', '-{}.html'.format(page))
            params = self.params.copy()
            if self.params.get('page', None):
                params.update({'page': page})
            page_urls.append((self._make_url(url), params))

        # Scrape pages in parallel
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()*2)

        for page in pool.map(scrape_helper, page_urls):
            self.soup = BeautifulSoup(page, 'lxml')

            results += [
                SmartPriceResult(self.get_product_attrs(item))
                for item in self.products_html
                ]
        return results

    @property
    def get_page_range(self):
        page_range = self.soup.findAll(
            'span', attrs={'class': 'pgntn__rslt-page'})

        if not page_range:
            return None

        first_page = int(page_range[0].text)
        last_page = int(page_range[1].text)
        return first_page, last_page

