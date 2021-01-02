# Created by volos at 12/30/2020
Feature: Footer functionality
  # Footer shows Best Selling, Latest, Top Rated categories
  # All products in the footer have price, name, star-rating
  # "Copyright 2020" shown in footer
  # TODO: Footer has button to go back to top ???
  # Footer has working links to all product categories

  Scenario: Footer shows Best Selling category
    Given Open Home page
    Then  Verify BEST SELLING category

  Scenario: Footer shows Latest category
    Given Open Home page
    Then  Verify LATEST category

  Scenario: Footer shows Top Rated category
    Given Open Home page
    Then  Verify TOP RATED category

  Scenario: "Copyright 2020" shown in footer
    Given Open Home page
    Then  Verify "Copyright 2020" shown in footer

  Scenario: Open category
    Given Open Home page
    When  Click on category "ACCESSORIES" on Footer menu
    Then  Verify category "AirPods" is opened

  Scenario: Open category
    Given Open Home page
    When  Click on category "WATCH" on Footer menu
    Then  Verify category "Watch" is opened

  Scenario: Open category
    Given Open Home page
    When  Click on category "MAC" on Footer menu
    Then  Verify category "MacBook" is opened

  Scenario: All products on Top Rated category has titles
    Given Open Home page
    Then  Verify titles of all products in the TOP RATED category

  Scenario: All products on Latest category has titles
    Given Open Home page
    Then  Verify titles of all products in the LATEST category
