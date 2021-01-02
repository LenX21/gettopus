from behave import then, when
from behave import use_step_matcher

use_step_matcher("re")


@then('Verify Empty Cart page shows "(?P<search_text>[\w\s]+\.?)" message')
def empty_cart(context, search_text):
    context.app.cart_page.verify_cart_is_empty(search_text)


@then("Verify Shopping Cart is opened")
def verify_current_state(context):
    context.app.cart_page.current_state()


@then('Verify "(?P<cart_state>Shopping Cart|Checkout Details|Order Complete)" is opened')
def verify_current_state(context, cart_state):
    context.app.cart_page.current_state(cart_state)
