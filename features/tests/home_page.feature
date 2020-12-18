# Created at 12/15/2020
Feature: Home page functionality
  # User can click right and left arrows to see top banners;
  # User can click bottom dots to see top banners
  # User can click on product banner and is taken to correct category page

  @top_banner
  Scenario: Top Banner click on RIGHT arrow
    Given Open Home page
    When  Click on "NEXT" arrow
    Then  Make sure the banner has been changed

  @top_banner, @smoke
  Scenario: Top Banner click on LEFT arrow
    Given Open Home page
    When  Click on "PREV" arrow
    Then  Make sure the banner has been changed

  @top_banner, @smoke
  Scenario: Top Banner click on 1 dot
    Given   Open Home page
    When    Click on dot number "1" Top Banner Home page
    Then    Verify dot with number "1" is selected

  @top_banner, @smoke
  Scenario: Top Banner click on 2 dot
    Given   Open Home page
    When    Click on dot number "2" Top Banner Home page
    Then    Verify dot with number "2" is selected

  @top_banner, @smoke
  Scenario: Top Banner navigate to category page by clicking on banner
    Given   Open Home page
    Then    Verify sure clicking on the product banners redirects to the correct category page


# TODO:
#  @top_banner, @smoke
#  Scenario: Top Banner change active banner by clicking dots
#    Given   Open Home page
#    When    Select a dot other than the currently active
#    Then    Make sure the banner has been changed


