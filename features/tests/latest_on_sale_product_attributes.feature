# Created by volos at 12/17/2020
Feature: "Latest Products on Sale" category Product Attributes: Image, Name, Product Category, Price, Sale icon and Star rating
  # Every product has Sale icon, image, product category, name, price, and star-rating
  # Attributes are: IMAGE, NAME, CATEGORY, PRICE, ONSALE icon and Star RATING

  Scenario: All Products on sale have required attributes: Name of Product
    Given   Open Home page
    Then    Verify Products "Latest products on sale" category have "NAME" attribute

  Scenario: All Products on sale have required attributes: Image of Product
    Given   Open Home page
    Then    Verify Products "Latest products on sale" category have "IMAGE" attribute

  Scenario: All Products on sale have required attributes: Product Category
    Given   Open Home page
    Then    Verify Products "Latest products on sale" category have "CATEGORY" attribute

  Scenario: All Products on sale have required attributes: Price
    Given   Open Home page
    Then    Verify Products "Latest products on sale" category have "PRICE" attribute

  Scenario: All Products on sale have required attributes: On sale Icon
    Given   Open Home page
    Then    Verify Products "Latest products on sale" category have "ONSALE" attribute

  Scenario: All Products on sale have required attributes: Star Rating
    Given   Open Home page
    Then    Verify Products "Latest products on sale" category have "RATING" attribute