from behave import then, when, given
from behave import use_step_matcher

use_step_matcher("re")

@given('Open Product page')
def open_product_page(context):
    context.app.product_page.open_product_page()

@then('Verify product page for "(?P<search_text>[\w\s]+)" is opened')
def verify_product_data(context, search_text):
    context.app.product_page.verify_product_title(search_text)


# @then('Verify search result shows "(?P<search_text>[\w\s[:punct:]]+)"')
@then('Verify search result shows "(?P<search_text>[\w\s]+\.?)"')
def verify_search_result_is_empty(context, search_text):
    context.app.product_page.verify_empty_search_result(search_text)


@when(u'Chose product "(?P<search_text>.+)" from category list by name')
def verify_product_data(context, search_text):
    context.app.product_category_page.open_product_page(product_name=search_text)
    # context.app.product_page.verify_product_data()

@when(u'Chose product "(?P<search_number>[\d]+)" from category list by number')
def verify_product_data(context, search_number):
    context.app.product_category_page.open_product_page(product_number=int(search_number))
    # context.app.product_page.verify_product_data()

@when("Add product to card")
def add_product_to_cart(context):
    context.app.product_page.add_product_to_cart()
    try:
        context.current_price += context.app.product_page.get_product_price()
    except AttributeError:
        context.current_price = context.app.product_page.get_product_price()
    try:
        context.products_titles.append(context.app.product_page.products_titles())
    except AttributeError:
        context.products_titles = [context.app.product_page.products_titles()]


@then("Verify Product has Title, Image, Price and Description")
def verify_product_data(context):
    context.app.product_page.verify_product_data()


@when("Zoom in product image")
def zoom_in_product_image(context):
    context.app.product_page.zoom_in_product_image()

@when("Close zoom in image")
def close_zoom_in_image(context):
    context.app.product_page.zoom_in_product_image()


@when("Switch between zoomed in the images")
def step_impl(context):
    context.app.product_page.swipe_between_zoom_in_images()