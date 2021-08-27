Feature: Shopping cart
  As a visitor of the ecommerce website
  I want to have a shopping cart
  So that I can see the products and costs of what I want to
  purchase

  Scenario: cart01 - Opening the shopping cart
    Given I have added an item to my shopping bag
    When I click the shopping bag icon
    Then I land on the shopping bag page
    And I can see the product in my shopping cart

  Scenario: cart02 - Adding a product to cart
    Given I am on a product detail page
    When I select the amount
    And I click the add to cart button
    Then the product is added to my shopping cart
