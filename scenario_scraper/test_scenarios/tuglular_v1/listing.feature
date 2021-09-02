Feature: Product lister page
  As a visitor of the ecommerce website
  I want to see an overview of products
  So that I can select a product that fits my needs

  Scenario: plp01 - Navigating to a Product lister page

    Given I am on the homepage where I can go to a product lister page #atHome
    When I select a Product lister page from the menu
    Then I am on the Product lister page #productList

  Scenario: plp02 - Filtering on the Product lister page
    Given I am on a Product lister page #productList
    When I select the filter (...)
    And I click the button to confirm filtering
    Then the page is filtered to only show (...) products #filteredProductList
