from dataclasses import dataclass
from typing import Dict, Tuple

from strenum import StrEnum


class EnvironmentData:
    CHROME_EXECUTABLE_PATH = 'tools\chromedriver.exe'
    EDGE_EXECUTABLE_PATH = 'tools\msedgedriver.exe'
    REPORTING_FOLDER = 'reporting'


@dataclass
class ItemDescription:
    # name: str
    title: str
    subpath: str = ''

    @property
    def path(self):
        if self.subpath:
            return f'{self.subpath}/{self.name}'
        return f'{self.name}'

    # def title(self):
    #     return self.customTitle
    @property
    def name(self):
        return self.title.lower()

    @property
    def product_category(self):
        if self.subpath:
            return self.subpath.upper()
        return self.title.upper()


class TestData:
    BASE_URL: str = 'https://gettop.us/'
    PRODUCT_CATEGORY_PARTIAL_LINK: str = 'product-category'
    PRODUCT_CATEGORIES: Dict[str, ItemDescription] = {
        'ipad': ItemDescription('iPad'),
        'macbook': ItemDescription('MacBook'),
        'iphone': ItemDescription('iPhone'),
        'airpods': ItemDescription('AirPods', subpath='accessories'),
        'watch': ItemDescription('Watch', subpath='accessories'),
        'accessories': ItemDescription('Accessories')
    }
    PRODUCT_CATEGORY_URL = f'{BASE_URL}{PRODUCT_CATEGORY_PARTIAL_LINK}'

    @staticmethod
    def get_product_link_by_name(category_name: str):
        return f'{TestData.PRODUCT_CATEGORY_URL}/{TestData.PRODUCT_CATEGORIES[category_name.lower()].path}'


class Directions(StrEnum):
    NEXT = 'next'
    PREV = 'previous'

# class ProductAttributes(StrEnum):
#     NAME = 'p.name.product-title'
#     CATEGORY = 'p.category.uppercase'
#     IMAGE = 'img[src*="https"]'
#     PRICE = 'span.price'
#     ONSALE = 'span.onsale'
#     RATING = 'div.star-rating'
