# Created by volos at 12/30/2020
Feature: # Enter feature name here
  # Product has image, name, price, description
  # User can zoom in product image, scroll thru images and close them (by clicking X)
  # User can add product to wishlist by hovering over product image and clicking on the heart icon
  # "Home" link takes user to Home PageCategory link (i.e. iPhone) takes users to correct category page
  # Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn
  # Clicking on a social network link opens a new window to login to social network

#  User can add product to cartUser can click - and + to modify amount of items to add to cart, upon adding to cart, correct amount of items shown in the cartUser can type in amount of items to add to cart, upon adding to cart, correct amount of items shown in the cartUser sees " ... have been added to your cart" confirmation upon adding items to cartUser can click through multiple products by clicking back and forward arrowsIf product is out of stock, user sees 'Out of Stock', Add to Cart and Checkout buttons are not shown (https://gettop.us/product/land-tee-jack-jones/)
#"You may also like…" bock is shown and contains products
# Product links under "You may also like…" bock are clickable and take to correct pages

#  Description block is shown
#User can submit a review
# Correct amount of product reviews are shown

  Scenario: Product has image, name, price and description
    Given Open Product page
    Then  Verify Product has Title, Image, Price and Description

  Scenario: Zoom in product image and close it
    Given Open Product page
    When  Zoom in product image
    And   Switch between zoomed in the images
    And   Close zoom in image
