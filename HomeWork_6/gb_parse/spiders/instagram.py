from urllib.parse import urlencode

import scrapy
import json
import datetime

from gb_parse.items import GbInstaTagItem


class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['www.instagram.com']
    start_urls = ['https://www.instagram.com/']
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    _tags_url = '/explore/tags/'
    _api_url = '/graphql/query/'

    query_hash = '9b498c08113f1e09617a1703c22b2f32'

    def __init__(self, login, password, tags, *args, **kwargs):
        self.login = login
        self.password = password
        self.tags = tags
        super().__init__(*args, **kwargs)

    def parse(self, response):
        try:
            js_data = self.js_data_extract(response)
            yield scrapy.FormRequest(
                self.login_url,
                method="POST",
                callback=self.parse,
                formdata={
                    'username': self.login,
                    'enc_password': self.password
                },
                headers={'X-CSRFToken': js_data['config']['csrf_token']}
            )
        except AttributeError as err:
            print(err)
            for tag_name in self.tags:
                yield response.follow(f"{self._tags_url}{tag_name}/", callback=self.tag_page_parse)

    def tag_page_parse(self, response):
        js_data = self.js_data_extract(response)
        hashtag = js_data['entry_data']['TagPage'][0]['graphql']['hashtag']
        yield self.get_tag_item(hashtag)
        yield from self.get_post_items(hashtag)
        yield response.follow(f"{self._api_url}?{urlencode(self.paginate_params(hashtag))}", callback=self.api_tag_parse)

    def api_tag_parse(self, response):
        data = response.json()
        hashtag = data['data']['hashtag']
        yield from self.get_post_items(hashtag)
        yield response.follow(f"{self._api_url}?{urlencode(self.paginate_params(hashtag))}", callback=self.api_tag_parse)

    def js_data_extract(self, response):
        script = response.xpath("//script[contains(text(), 'window._sharedData =')]/text()").extract_first()
        return json.loads(script.replace('window._sharedData = ', '')[:-1])

    def get_tag_item(self, hashtag):
        item = GbInstaTagItem()
        item['collection_name'] = 'ItemTag'
        item['date_parse'] = datetime.datetime.utcnow()
        data = {}
        for key, value in hashtag.items():
            if not (isinstance(value, dict) or isinstance(value, list)):
                data[key] = value
        item['data'] = data
        return item

    def paginate_params(self, hashtag):
        variables = {
            'tag_name': hashtag['name'],
            'first': 100,
            'after': hashtag['edge_hashtag_to_media']['page_info']['end_cursor']

        }

        url_query = {
            'query_hash': self.query_hash,
            'variables': json.dumps(variables)
        }
        return url_query

    def get_post_items(self, hashtag):
        for edge in hashtag['edge_hashtag_to_media']['edges']:
            yield GbInstaTagItem(collection_name='ItemPost', date_parse=datetime.datetime.utcnow(), data=edge['node'])

