# Created by volos at 12/23/2020
Feature: Top navigation menu
  # GETTOP LOGO
  # GetTop logo is clickable and takes to https://gettop.us/

  # SEARCH
  # User can search for existing product and sees correct results
  # User can search for non-existing product and sees "No products were found matching your selection."

  # PRODUCT CATEGORIES
  # User can hover over Mac and see correct menu options
  # User can hover over iPhone and see correct menu options
  # User can hover over iPad and see correct menu options
  # User can hover over Watch and see correct menu options
  # User can hover over Accessories and see correct menu options
  # User can select Mac product from top menu and correct page opens
  # User can select iPhone product from top menu and correct page opens
  # User can select iPad product from top menu and correct page opens
  # User can select Watch product from top menu and correct page opens
  # User can select Accessories product from top menu and correct page opens

  # ACCOUNT
  # Clicking on Account icon opens Login form

  # CART
  # Clicking on Cart icon opens Empty Cart page if no products were added
  # Hovering over empty cart icon shows "No products in the cart." message
  # Add product to cart, verify that price in top nav menu is correct
  # Add products to cart, verify that amount of items shown in top nav menu are correct
  # Add products to cart, hover over cart icon, verify correct products and subtotal shown
  # Add products to cart, hover over cart icon, verify user can click on "View Cart" and is taken to cart page
  # Add products to cart, hover over cart icon, verify user can click on "Checkout" and is taken to checkout page
  # Add a product to cart, hover over cart icon, verify user can remove a product


  Scenario: GetTop logo redirects to home page
    Given Open "WATCH" product category page
    When  Click on LOGO icon on Top menu
    Then  Verify home page is opened

  Scenario: GetTop logo redirects to home page
    Given Open "MACBOOK" product category page
    When  Click on LOGO icon on Top menu
    Then  Verify home page is opened

  Scenario: Search for existing product "MacBook Air"
    Given Open Home page
    When  Search for product "MacBook Air"
    Then  Verify product page for "MacBook Air" is opened

  Scenario: Search for non-existing product "MacBook Air"
    Given Open Home page
    When  Search for product "Lenovo"
    Then  Verify search result shows "No products were found matching your selection."

  Scenario: Hover over iPad category on the Top menu is shown options menu
    Given   Open Home page
    When    Hover over "IPAD" category on Top menu
    Then    Options menu is shown for "IPAD"

  Scenario: Hover over Mac category on the Top menu is shown options menu
    Given   Open Home page
    When    Hover over "MAC" category on Top menu
    Then    Options menu is shown for "MAC"

  Scenario: Open product category by clicking on category name on Top menu
    Given   Open Home page
    When    Click on category "ACCESSORIES" on Top menu
    Then    Verify category "AirPods" is opened

  Scenario: Open product category by clicking on category name on Top menu
    Given   Open Home page
    When    Click on category "WATCH" on Top menu
    Then    Verify category "Watch" is opened

  Scenario: Open product category by clicking on category name on Top menu
    Given   Open Home page
    When    Click on category "MAC" on Top menu
    Then    Verify category "MacBook" is opened

  Scenario: Open Login Form by clicking on Account icon on Top menu
    Given   Open Home page
    When    Click on ACCOUNT icon on Top menu
    Then    Verify Login Form is opened

  Scenario: Cart icon opens Empty Cart page if no products were added
    Given   Open Home page
    When    Click on CART icon on Top menu
    Then    Verify Empty Cart page shows "Your cart is currently empty." message

  Scenario: Empty cart icon shows "No products in the cart." message
    Given   Open Home page
    When    Hover over "PRICE" icon on Top menu
    Then    Verify Empty Cart icon shows "No products in the cart." message

#  Scenario: Correct price of product added to cart is shown on Top menu
#    Given Open "MACBOOK" product category page
#    When  Chose product "1" from category list by number
#    When  Chose product "MacBook Pro 13-inch" from category list by name
#    Then  Verify Cart Price shows correct price

  Scenario: Correct price of product added to cart is shown on Top menu for "MacBook Air"
    Given Open Home page
    When  Search for product "MacBook Air"
    When  Add product to card
    Then  Verify product price is shown Top menu is correct

  Scenario: Amount of product added to cart is shown on Top menu for "MacBook Air"
    Given Open Home page
    When  Search for product "MacBook Air"
    When  Add product to card
    Then  Cart icon shows "1" product(s)

  Scenario: Products title and subtotal are shown on Top menu for products added to cart
    Given Open "MACBOOK" product category page
    When  Chose product "2" from category list by number
    And   Add product to card
    When  Search for product "MacBook Air"
    When  Add product to card
    And   Hover over "CART" icon on Top menu
    Then  Verify content of tooltip for cart icon

  Scenario: Cart page is opened after clicking "View Cart" button from Top Menu tooltip
    Given Open "MACBOOK" product category page
    When  Chose product "2" from category list by number
    And   Add product to card
    And   Hover over "CART" icon on Top menu
    And   Open Cart by clicking "View Cart" button on Top Menu
    Then  Verify Cart is open