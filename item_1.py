import requests
import bs4
from urllib.parse import urljoin
import pymongo
import datetime

list_months = ['', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

def get_date(str_date):
    list_str_date = str_date.replace('с ', '').replace('до ', '').splitlines(keepends=False)
    list_date = []
    year = datetime.datetime.now().year

    for date in list_str_date:
        if date:
            value_date = date.split()
            day = int(value_date[0])
            value_month = value_date[1][:3]

            for i, month in enumerate(list_months):
                if (month == value_month):
                    month_number = i
                    break

            list_date.append(datetime.date(year, month_number, day).strftime('%d/%m/%Y'))

    return list_date

class MagnitParse:
    def __init__(self, start_url, db_client):
        self.start_url = start_url
        self.db = db_client['DB_Magnit_230221']
        self.collection = self.db['magnit_promo']

    def _get_response(self, url):
        return requests.get(url)

    def _get_soup(self, url):
        response = self._get_response(url)
        return bs4.BeautifulSoup(response.text, 'lxml')

    def run(self):
        soup = self._get_soup(self.start_url)
        catalog = soup.find("div", attrs={'class': "сatalogue__main"})
        for prod_a in catalog.find_all('a', recursive=False):
            product_data = self._parse(prod_a)
            self._save(product_data)

    def get_template(self):
        return {
            'url': lambda a: urljoin(self.start_url, a.attrs.get('href', '')),
            'promo_name': lambda a: a.find('div', attrs={'class': 'card-sale__name'}).text,
            'product_name': lambda a: a.find('div', attrs={'class': 'card-sale__title'}).text,
            'old_price': lambda a: float('.'.join(a.find("div", attrs={'class': "label__price label__price_old"}).text.split())),
            'new_price': lambda a: float('.'.join(a.find("div", attrs={'class': "label__price label__price_new"}).text.split())),
            'image_url': lambda a: a.find('img').attrs.get('data-src'),
            'date_from': lambda a: get_date(a.find('div', attrs={'class': 'card-sale__date'}).text)[0],
            'date_to': lambda a: get_date(a.find('div', attrs={'class': 'card-sale__date'}).text)[1]
        }

    def _parse(self, product_a) -> dict:
        data = {}
        for key, func in self.get_template().items():
            try:
                data[key] = func(product_a)
            except ValueError:
                pass
            except AttributeError:
                pass
        return data

    def _save(self, data: dict):
        self.collection.insert_one(data)


if __name__ == '__main__':
    url = 'https://magnit.ru/promo/'
    db_client = pymongo.MongoClient('mongodb://localhost:27017')
    parser = MagnitParse(url, db_client)
    parser.run()
