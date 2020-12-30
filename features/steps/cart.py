from behave import then, when
from behave import use_step_matcher

use_step_matcher("re")


@then('Verify Empty Cart page shows "(?P<search_text>[\w\s]+\.?)" message')
def empty_cart(context, search_text):
    context.app.cart_page.verify_cart_is_empty(search_text)


@then("Verify Cart is open")
def verify_current_state(context):
    context.app.cart_page.current_state()