from behave import then, when
from behave import use_step_matcher

use_step_matcher("re")


@then('Verify (?P<category_name>BEST SELLING|LATEST|TOP RATED) category')
def verify_best_selling(context, category_name):
    context.app.footer_menu.verify_category_content_is_not_empty(category_name)


@then('Verify "(?P<search_text>[\w\s]+)" shown in footer')
# @then('Verify "(?P<search_text>[\w\s]+)" shown in footer')
def copyrights_footer(context, search_text):
    context.app.footer_menu.verify_copyright(search_text)

@when('Click on category "(?P<category>MAC|IPHONE|IPAD|WATCH|ACCESSORIES)" on Footer menu')
def open_category_top_menu(context, category):
    context.app.footer_menu.open_category(category)


@then('Verify titles of all products in the (?P<category_name>BEST SELLING|LATEST|TOP RATED) category')
def step_impl(context, category_name):
    context.app.footer_menu.verify_products_attribute(category_name)