from behave import given, then, when
from behave import use_step_matcher

use_step_matcher("re")


@given('Open "(?P<category>MACBOOK|IPHONE|IPAD|WATCH|AIRPODS|ACCESSORIES)" product category page')
def open_product_category_page(context, category):
    context.app.product_category_page.open_product_category_page_by_name(category)


@then('Verify category "(?P<category_title>[\w\s]+)" is opened')
def verify_category_is_opened(context, category_title):
    context.app.product_category_page.correct_category_is_opened(category_title.upper().strip())
    # context.app.product_category_page.verify_category_is_opened(category_title.upper().strip())



@when('Click on category "(?P<category_title>[\w\s]+)"')
def open_category_by_name(context, category_title):
    context.app.home_page.open_category_by_name(category_title.strip())


@when('Open "(?P<category>MAC|IPHONE|IPAD|WATCH|ACCESSORIES)" category from Top menu')
def open_category_top_menu_by_name(context, category):
    context.app.top_menu.open_category_by_name(category)


@when('Search for product "(?P<search_text>[\w\s]+)"')
def search_product(context, search_text):
    context.app.top_menu.search_product(search_text)


@when('Hover over "(?P<category>MAC|IPHONE|IPAD|WATCH|ACCESSORIES)" category on Top menu')
def hover_over_category_top_menu(context, category):
    context.app.top_menu.hover_over_category_top_menu(category)

@when('Hover over "(?P<icon_name>LOGO|SEARCH|ACCOUNT|PRICE|CART)" icon on Top menu')
def hover_over_category_top_menu(context, icon_name):
    context.app.top_menu.hover_over_icon(icon_name)

@when('Click on category "(?P<category>MAC|IPHONE|IPAD|WATCH|ACCESSORIES)" on Top menu')
def open_category_top_menu(context, category):
    context.app.top_menu.open_category_by_name(category)


@then(f'Options menu is shown for "(?P<category>MAC|IPHONE|IPAD|WATCH|ACCESSORIES)"')
def options_menu_is_shown(context, category):
    context.app.top_menu.verify_all_products_from_dd(category)

@when('Click on (?P<icon_name>LOGO|ACCOUNT|CART|SEARCH) icon on Top menu')
def click_account_icon(context, icon_name):
    context.app.top_menu.click_icon(icon_name)


@then('Verify Empty Cart icon shows "(?P<search_text>[\w\s]+\.?)" message')
def verify_empty_cart_icon_message_(context, search_text):
    context.app.top_menu.verify_empty_cart_message(search_text)


@then("Verify product price is shown Top menu is correct")
def verify_top_menu_price(context):
    context.app.top_menu.verify_price(context.current_price)


@then('Cart icon shows "(?P<amount_of_products>[\d]+)" product\(s\)')
def verify_cart_icon_amount_of_added_products(context, amount_of_products):
    context.app.top_menu.cart_icon_amount_of_added_product(int(amount_of_products))


@then("Verify content of tooltip for cart icon")
def tooltip_cart_content(context):
    context.app.top_menu.verify_tooltip_subtotal_sum(context.current_price)
    context.app.top_menu.verify_tooltip_products_added_to_cart(context.products_titles)


@when('Open Cart by clicking "View Cart" button on Top Menu')
def click_view_cart_button(context):
    context.app.top_menu.open_cart_page()


@when('Click "(?P<icon_name>VIEW CART|CHECKOUT)" button on Top Menu')
def step_impl(context, icon_name):
    context.app.top_menu.open_cart_tooltip(len(context.products_titles), icon_name)


@when('Remove "(?P<product_name>[\w\s]+)" product from Cart Top Menu')
def step_impl(context, product_name):
    context.app.top_menu.remove_product_by_name(product_name)