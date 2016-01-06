from pysmartprice.abstract import(
    BaseParser,
    ParserMixin
)


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
