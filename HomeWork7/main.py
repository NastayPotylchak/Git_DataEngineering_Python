from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from gb_parse.spiders.autoyoula import AutoyoulaSpider
from gb_parse.spiders.instagram import InstagramSpider
import os
import dotenv

if __name__ == '__main__':
    dotenv.load_dotenv('.env')
    crawler_settings = Settings()
    tags = ['python']
    users = ['geekbrains.ru']
    crawler_settings.setmodule('gb_parse.settings')
    crawler_proc = CrawlerProcess(settings=crawler_settings)
    # crawler_proc.crawl(AutoyoulaSpider)
    crawler_proc.crawl(InstagramSpider,
                       login=os.getenv('INST_LOGIN'),
                       password=os.getenv('INST_PASSWORD'),
                       tags=tags,
                       users=users
                       )
    crawler_proc.start()


