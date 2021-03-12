import scrapy
from ..loaders import AutoYoulaLoader
import re


class AutoyoulaSpider(scrapy.Spider):
    name = 'autoyoula'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['http://auto.youla.ru/']

    _xpath_selectors = {
        'brands': "//div[@data-target='transport-main-filters']/div"
                  "[contains(@class, 'TransportMainFilters_brandsList')]"
                  "//a[@data-target='brand']/@href",
        'pagination': "//a[@data-target-id='button-link-serp-paginator']/@href",
        'car': "//article[@data-target='serp-snippet']//a[@data-target='serp-snippet-title']/@href"
    }

    _car_xpaths = {
        'title': "//div[@data-target='advert-title']/text()",
        'list_imgs': "//figure/picture/img/@src",
        'characteristics': "//h3[contains(text(), 'Характеристики')]/..//div[contains(@class, 'AdvertSpecs_row')]",
        'descriptions': "//div[@data-target='advert']//div[@data-target='advert-info-descriptionFull']/text()"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_follow(self, response, select_str, callback, **kwargs):
        for link in response.xpath(select_str):
            yield response.follow(link, callback=callback, cb_kwargs=kwargs)

    def parse(self, response, *args, **kwargs):
        yield from self._get_follow(response, self._xpath_selectors['brands'], self.brand_parse)

    def brand_parse(self, response, **kwargs):

        yield from self._get_follow(response, self._xpath_selectors['pagination'], self.brand_parse)

        yield from self._get_follow(response, self._xpath_selectors['car'], self.car_parse)

    def car_parse(self, response):
        loader = AutoYoulaLoader(response=response)
        loader.add_value('url', response.url)

        for key, xpath in self._car_xpaths.items():
            loader.add_xpath(key, xpath)

        yield loader.load_item()

