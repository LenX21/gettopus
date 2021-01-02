# Created by volos at 12/30/2020
Feature: # Enter feature name here
  # Only items of correct category are shown"
  # Showing all <N> results" is present and reflects correct amount of items
  # (count amount of products on the page to verify this)
  # All items have Category, Name and Price
  # User can open and close Quick View by clicking on closing X
  # User can click Quick View and add product to cart

  Scenario: Only products that have 'Macbook' category are shown
    Given   Open "MACBOOK" product category page
    Then    Verify that only products from the "MACBOOK" category are shown

  Scenario: Only products that have 'iPhone' category are shown
    Given   Open "IPHONE" product category page
    Then    Verify that only products from the "IPHONE" category are shown

  Scenario: Only products that have 'iPad' category are shown
    Given   Open "IPAD" product category page
    Then    Verify that only products from the "IPAD" category are shown

  Scenario: Only watches that have 'ACCESSORIES' category are shown
    Given   Open "WATCH" product category page
    Then    Verify that only products from the "ACCESSORIES" category are shown

  Scenario: Only airPods that have 'ACCESSORIES' category are shown
    Given   Open "AIRPODS" product category page
    Then    Verify that only products from the "ACCESSORIES" category are shown


  Scenario: Amount of products are shown pre page for 'Macbook' category
    Given   Open "MACBOOK" product category page
    Then    Verify the number of products per page

  Scenario: All products on the page have 'AIRPODS' in the name
    Given   Open "AIRPODS" product category page
    Then    Verify all products on the page contain "AIRPODS" in name

  Scenario: Open quick view for product "MacBook" category
    Given   Open "MACBOOK" product category page
    When    Open on Quick View for product "2"

  Scenario: Add product from quick View to cart
    Given   Open "WATCH" product category page
    When    Open on Quick View for product "2"
    And     Click "Add to Cart" button on Quick View
    Then    Cart icon shows "1" product(s)

  Scenario: Close Quick View by clicking X button
    Given   Open "MACBOOK" product category page
    When    Open on Quick View for product "2"
    And     Click on X to close Quick View
    Then    Verify Quick View is closed
