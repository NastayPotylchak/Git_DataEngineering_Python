import requests
from pathlib import Path
import time
import json

class Parse_Products:
    url_products = 'https://5ka.ru/api/v2/special_offers/'
    headers_5ka = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36'}

    def __init__(self, product_url: str, save_path_sale_products: Path):
        self.product_url = product_url
        self.save_path_sale_products = save_path_sale_products

    def _get_response(self, url):
        while True:
            response = requests.get(url, headers=self.headers_5ka)
            if response.status_code == 200:
                return response
            time.sleep(0.5)

    def run(self):
        for product in self._parse(self.product_url):
            product_path = self.save_path_sale_products.joinpath(f"{product['id']}.json")
            self._save(product, product_path)

    def _parse(self, url):
        while url:
            response = self._get_response(url)
            data = response.json()
            url = data['next']
            for product in data['results']:
                yield product

    def save(self, data: dict, file_path: Path):
        file_path.write_text(json.dumps(data, ensure_ascii=False), encoding='UTF-8')

class Parse_Categories(Parse_Products):
    url_categories = 'https://5ka.ru/api/v2/categories/'

    def __init__(self, product_url, save_path_sale_products, url_categories):
        super().__init__(product_url, save_path_sale_products)
        self.url_categories = url_categories

    def _get_categories(self):
        response = self._get_response(self.url_categories)
        data = response.json()
        return data

    def run(self):
        for category in self._get_categories():
            category['sale_products'] = []
            url = f"{self.product_url}?categories={category['parent_group_name']}"
            for product in self._parse(url):
                category['sale_products'].append(product)
                print(product)

            category_save_path = self.save_path_sale_products.joinpath(f"{category['parent_group_name']}.json")
            self.save(category, category_save_path)

if __name__ == '__main__':

    save_path_categories = Path(__file__).parent.joinpath('categories')
    if not save_path_categories.exists():
        save_path_categories.mkdir()

    categories_parser = Parse_Categories(Parse_Products.url_products,
                                         save_path_categories,
                                         Parse_Categories.url_categories
                                        )

    categories_parser.run()