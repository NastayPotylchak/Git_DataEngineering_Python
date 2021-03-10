import scrapy
import pymongo


class AutoyoulaSpider(scrapy.Spider):
    name = 'autoyoula'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['http://auto.youla.ru/']

    _css_selectors = {
        'brands': '.TransportMainFilters_brandsList__2tIkv '
                  '.ColumnItemList_container__5gTrc '
                  'a.blackLink',
        'pagination': 'a.Paginator_button__u1e7D',
        'car': '.SerpSnippet_titleWrapper__38bZM a.SerpSnippet_name__3F7Yu'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_client = pymongo.MongoClient('mongodb://localhost:27017')
        self.collection = 'autoyoula_cars_info'

    def _get_follow(self, response, select_str, callback, **kwargs):
        for a in response.css(select_str):
            link = a.attrib.get('href')
            yield response.follow(link, callback=callback, cb_kwargs=kwargs)

    def parse(self, response, *args, **kwargs):
        yield from self._get_follow(response,
                                    self._css_selectors['brands'],
                                    self.brand_parse,
                                    hello='moto'
                                    )

    def brand_parse(self, response, **kwargs):
        yield from self._get_follow(response,
                                    self._css_selectors['pagination'],
                                    self.brand_parse
                                    )

        yield from self._get_follow(response,
                                    self._css_selectors['car'],
                                    self.car_parse
                                    )

    def car_parse(self, response):
        cars_info = {}
        cars_characteristics = {}
        list_characteristics = []

        # Название объявления
        cars_info['title'] = response.css('.AdvertCard_advertTitle__1S1Ak::text').extract_first()

        # Список фото объявления (ссылки)
        list_img = [img.attrib.get('src') for img in response.css('figure.PhotoGallery_photo__36e_r img')]
        cars_info['list_imgs'] = list_img

        # Список характеристик
        for ch in response.css('div.AdvertCard_specs__2FEHc .AdvertSpecs_row__ljPcX'):
            cars_characteristics['name'] = ch.css('.AdvertSpecs_label__2JHnS::text').extract_first()
            cars_characteristics['value'] = ch.css('.AdvertSpecs_data__xK2Qx::text').extract_first()
            list_characteristics.append(cars_characteristics)

        cars_info['characteristics'] = list_characteristics

        # Описание объявления
        cars_info['descriptions'] = response.css('div.AdvertCard_descriptionInner__KnuRi::text').extract_first()

        #Сохранение в базу
        self.save_cars_info_to_mongo(cars_info)

    def save_cars_info_to_mongo(self, dict_info: dict):
        self.db_client["db_autoyoula_10_03_2021"][self.collection].insert_one(dict_info)

