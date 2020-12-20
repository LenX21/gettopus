from behave import given, when, then
from behave import use_step_matcher

use_step_matcher("re")


@given('Open Home page')
def open_home_page(context):
    context.app.home_page.open_home_page()


@when(u'Click on "(?P<directions>NEXT|PREV)" arrow')
def click_on_right_arrow(context, directions):
    context.app.home_page.top_banner_arrow_click(directions)


@then('Make sure the banner has been changed')
def banner_has_been_changed(context):
    context.app.home_page.verify_banner_changed()


@when('Click on dot number "(?P<specific_number>\d+)" Top Banner Home page')
def banner_has_been_changed(context, specific_number):
    context.app.home_page.click_dot_by_number_on_top_banner(specific_number)


@then('Verify dot with number "(?P<specific_number>\d+)" is selected')
def verify_dot_with_specific_number_is_selected(context, specific_number):
    context.app.home_page.verify_dot_with_specific_number_is_selected(specific_number)


@when('Click on the "(?P<specific_number>\d+)" Top Banner Home page')
def click_on_top_banner_navigate_to_product_category(context, specific_number):
    context.app.home_page.click_dot_by_number_on_top_banner(specific_number)
    context.app.home_page.open_product_category_by_clicking_on_active_banner(open_in_new_window=True)


@then("Verify sure clicking on the product banners redirects to the correct category page")
def verify_all_banners_navigate_to_product_category(context):
    context.app.home_page.open_all_product_category_by_clicking_top_banner()


@then(u'Verify "(?P<section_title>[\w\s]+)" section is present')
def verify_section_title_home_page(context, section_title):
    context.app.home_page.verify_titles_of_content_sections(section_title)


@then('Verify Products "(?P<section_title>Latest products on sale)" category have "(?P<attribute>NAME|CATEGORY|PRICE|IMAGE|RATING|ONSALE)" attribute')
def verify_products_attributes_for_section_home_page(context, section_title, attribute):
    context.app.home_page.verify_product_mandatory_attribute(section_title, attribute)


@then(u'Verify Products in "(?P<section_title>Latest products on sale)" section have all required attributes')
def verify_products_attributes_for_section_home_page(context, section_title):
    context.app.home_page.verify_product_all_mandatory_attributes(section_title)


@when('Click on heart icon to add product "(?P<specific_product>\d+)" to wishlist')
def click_heart_icon_product_by_number(context, specific_product):
    context.app.home_page.add_product_on_sale_to_wishlist(int(specific_product))

@when('Open wishlist by clicking on heart icon')
def open_wish_list_by_clicking_heart_icon(context):
    context.app.home_page.open_wishlist()

@then('Verify that wishlist contains the product')
def verify_wishlist_contains(context):
    context.app.wishlist_page.verify_products_names()


@when('Click on product "(?P<specific_product>\d+)"')
def click_on_product_on_sale(context, specific_product):
    context.app.home_page.open_product_page_on_sale(int(specific_product))


@then("Verify that product page is opened and contains product price and description")
def verify_product_data(context):
    context.app.product_page.verify_product_data()

@when('Click on Quick View for product "(?P<specific_product>\d+)"')
def click_on_quick_view_link(context, specific_product):
    context.app.home_page.open_quick_view_product_on_sale(int(specific_product))


@when("Click on X to close Quick View")
def close_quick_view_by_clicking_x(context):
    context.app.home_page.close_quick_view_x()


@then("Verify all images available for preview on Quick View")
def verify_quick_view_images(context):
    context.app.home_page.switch_between_quick_view_images()
