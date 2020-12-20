# Created at 12/16/2020
Feature: "Latest Products on Sale" category Product Attributes Home Page
  # "Latest Products on Sale" text is shown
  #  Every product has Sale icon, image, product category, name, price, and star-rating
  #  User can click on heart icon to add to wishlist
  @TODO: # User can open product from Sale and add it to cart
  #  User can open product from Sale and see product price and description
  #User can open and close Quick View by clicking on closing X
  #User can click Quick View and add product to cart
  #User can click Quick View and click through product images

  Scenario: "Latest Products on Sale" text is shown
    Given   Open Home page
    Then    Verify "Latest products on sale" section is present

  Scenario: All Products from "Latest Products on Sale" have required attributes
    Given   Open Home page
    Then    Verify Products in "Latest products on sale" section have all required attributes

    # TODO what is the best way to do it: Try yo add all products, product specified by number(name) or any random product
  Scenario: The Product from "Latest Products on Sale" added to wishlist by clicking on heart icon
    Given   Open Home page
    When    Click on heart icon to add product "1" to wishlist
    And     Open wishlist by clicking on heart icon
    Then    Verify that wishlist contains the product


  Scenario: Open product page for the product from "Latest Products on Sale"
    Given   Open Home page
    When    Click on product "1"
    Then    Verify that product page is opened and contains product price and description

  Scenario: Open quick view for product "Latest products on sale" section
    Given   Open Home page
    When    Click on Quick View for product "3"
    And     Click on X to close Quick View

  Scenario: Add product from Quick View to card
    Given   Open Home page
    When    Click on Quick View for product "1"
#    And     Add product to card
#    Then    Verify the product is added to card

  Scenario: Add product from Quick View to card and check all images for product
    Given   Open Home page
    When    Click on Quick View for product "1"
    Then    Verify all images available for preview on Quick View






