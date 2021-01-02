from behave import then, when
from behave import use_step_matcher

use_step_matcher("re")


@then('Verify that only products from the "(?P<category>MACBOOK|IPHONE|IPAD|WATCH|ACCESSORIES)" category are shown')
def verify_all_product_in_category(context, category):
    context.app.product_category_page.verify_all_products_category(category)


@then("Verify the number of products per page")
def verify_amount_of_products(context):
    context.app.product_category_page.compare_number_products_shown_per_page()


@then('Verify all products on the page contain "(?P<search_text>[\w\s]+)" in name')
def step_impl(context, search_text):
    context.app.product_category_page.verify_all_products_contain_title(search_text)

