# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class GbParsePipeline:
    def process_item(self, item, spider):
        return item

class GbParseMongoPipeLine:

    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client['gb_parse_insta_21_03_2021']

    def process_item(self, item, spider):
        self.db['InstaUsers'].insert_one(item)
        return item

class GbImageDownloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        pass

