from scrapy.loader import ItemLoader
from .items import GbAutoYoulaItem
from itemloaders.processors import TakeFirst, MapCompose
from scrapy import Selector
import re
from base64 import b64decode

def get_characteristics(item):
    selector = Selector(text=item)
    data = {
        'name': selector.xpath("//div[contains(@class, 'AdvertSpecs_label')]/text()").extract_first(),
        'value': selector.xpath("//div[contains(@class, 'AdvertSpecs_data')]//text()").extract_first()
    }
    return data

def get_phone(item):
    if 'phone' in item:
        str_find_phone = re.compile(r"phone%22%2C%22([a-zA-Z|\d]+)%3D%3D%22%2C%22")
        phone = re.findall(str_find_phone, item)
        phone = b64decode(b64decode(f"{phone[0]}==")).decode('UTF-8')
    return phone

class AutoYoulaLoader(ItemLoader):
    default_item_class = GbAutoYoulaItem
    url_out = TakeFirst()
    title_out = TakeFirst()
    characteristics_in = MapCompose(get_characteristics)
    phone_in = MapCompose(get_phone)
