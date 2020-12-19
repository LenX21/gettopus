from strenum import StrEnum


class EnvironmentData:
    CHROME_EXECUTABLE_PATH = 'tools\chromedriver.exe'
    EDGE_EXECUTABLE_PATH = 'tools\msedgedriver.exe'
    REPORTING_FOLDER = 'reporting'


class TestData:
    BASE_URL = 'http://gettop.us/'
    PRODUCT_CATEGORY_PARTIAL_LINK = 'product-category'
    PRODUCT_CATEGORIES = {
        'ipad': 'iPad',
        'macbook': 'MacBook',
        'iphone': 'iPhone',
        'airpods': 'AirPods',
        'watch': 'Watch'
    }


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
