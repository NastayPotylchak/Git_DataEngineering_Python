from copy import deepcopy
from urllib.parse import urlencode

import scrapy
import json

import datetime

from gb_parse.items import GbInstaTagItem, GbInstaUserItem


class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['www.instagram.com']
    start_urls = ['https://www.instagram.com/']
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    _tags_url = '/explore/tags/'
    _api_url = '/graphql/query/'

    query_hash = '9b498c08113f1e09617a1703c22b2f32'

    def __init__(self, login, password, tags, users, *args, **kwargs):
        self.login = login
        self.password = password
        self.tags = tags
        self.users = users
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
            for user_name in self.users:
                yield response.follow(f"/{user_name}/", callback=self.user_page_parse)

    def user_page_parse(self, response):
        js_data = self.js_data_extract(response)
        user = InstUser(js_data['entry_data']['ProfilePage'][0]['graphql']['user'])
        yield user.get_user_item('followed_dict')
        yield response.follow(f"{self._api_url}?{urlencode(user.get_followed_vars())}",
                              callback=self._api_follow_parse,
                              cb_kwargs={'user': user})

    def _api_follow_parse(self, response, **kwargs):
        user = kwargs['user']
        yield user.get_user_item('followers_dict')

        yield response.follow(f"{self._api_url}?{urlencode(user.get_followed_vars())}",
                              callback=self._api_follow_parse)

class InstUser:
    def __init__(self, user):
        self.user = user
        self.user_followers = InstaFollowers(user['id'])

    def get_user_item(self, item_name):
        data = {}
        for key, value in self.user.items():
            if not (isinstance(value, dict) or isinstance(value, list)):
                data[key] = value

        return GbInstaUserItem(date_parse=datetime.datetime.utcnow(), item_name=data)

    def get_followed_vars(self):
        return self.user_followers.get_variables('followed')


class InstaFollowers:
    query_hashs = {
        "followed": {"query": "3dec7e2c57367ef3da3d987d89f9dbc8", "next": None},
        "followers": {"query": "5aefa9893005572d237da5068082d8d5", "next": None},
    }

    def __init__(self, user_id):
        self.user_id = user_id
        self.variables = {'id': user_id,
                          'include_reel': True,
                          'fetch_mutual': False,
                          'first': 24
                          }

    def get_variables(self, key):
        variables = deepcopy(self.variables)
        if self.query_hashs[key]["next"]:
            variables["after"] = self.query_hashs[key]["next"]

        url_query = {
            "query_hash": self.query_hashs[key]["query"],
            "variables": json.dumps(self.variables),
        }
        return url_query
