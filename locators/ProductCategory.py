from selenium.webdriver.common.by import By


class ProductCategoryLocators:
    PAGE_TITLE_ROW = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb.breadcrumbs.uppercase')
#     h1.product-title.product_title.entry-title
    PRODUCTS = (By.CSS_SELECTOR, 'div.product-small.col.has-hover.product.type-product')

