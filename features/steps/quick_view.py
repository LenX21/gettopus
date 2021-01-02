from behave import then, when
from behave import use_step_matcher

use_step_matcher("re")

@then('Verify Quick View for product "(?P<specific_product>\d+)" is opened')
def click_on_quick_view_link(context, specific_product):
    # context.app.quick_view.verify_quick_view_is_opened()
    context.app.quick_view.verify_quick_view_is_opened_for_product_by_number(int(specific_product))

@when('Open on Quick View for product "(?P<specific_product>\d+)"')
def click_on_quick_view_link(context, specific_product):
    # context.app.product_category_page.hover_over_product_by_number(int(specific_product))
    context.app.quick_view.open_quick_view_for_product_by_number(int(specific_product))

@when("Click on X to close Quick View")
def close_quick_view_by_clicking_x(context):
    context.app.quick_view.close_quick_view_x()


@then("Verify Quick View is closed")
def verify_quick_view_is_closed(context):
    context.app.quick_view.verify_quick_view_is_closed()


@when('Click "Add to Cart" button on Quick View')
def step_impl(context):
    context.app.quick_view.click_button_add_to_cart()