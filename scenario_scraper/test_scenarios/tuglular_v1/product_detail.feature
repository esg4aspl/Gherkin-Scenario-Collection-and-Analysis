Feature: Product detail page
  As a visitor of the ecommerce website
  I want to see the details of the product
  So that I know if the product fits my needs

  Scenario: pdp01 - Product detail page
    Given I am on a product lister page #productList
    When I select one of the items
    Then I am on the Product detail page of the selected item
    And I can see details of the product #productDetail
