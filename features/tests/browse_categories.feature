# Created by volos at 12/22/2020
Feature: Browse Our Categories
  # "Browse Our Categories" text is shown
  # 4 correct categories are shown
  # Upon clicking on each category, correct page opens

  Scenario: "Browse Our Categories" text is shown
    Given   Open Home page
    Then    Verify "Browse our Categories" section is present

  Scenario: 4 categories are shown on "Browse Our Categories" section
    Given   Open Home page
    Then    Verify "Browse our Categories" section contains "4" categories

  Scenario: Open page by clicking on category "Browse Our Categories" section
    Given   Open Home page
    When    Click on category "Accessories"
    Then    Verify category "Accessories" is opened

  Scenario: Open page by clicking on category "Browse Our Categories" section
    Given   Open Home page
    When    Click on category "iPad"
    Then    Verify category "iPad" is opened