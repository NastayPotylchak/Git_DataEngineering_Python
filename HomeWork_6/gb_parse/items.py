# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GbParseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GbAutoYoulaItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    list_imgs = scrapy.Field()
    characteristics = scrapy.Field()
    descriptions = scrapy.Field()
    phone = scrapy.Field()

class GbInstaTagItem(scrapy.Item):
    _id = scrapy.Field()
    date_parse = scrapy.Field()
    data = scrapy.Field()
    photos = scrapy.Field()
    collection_name = scrapy.Field()
