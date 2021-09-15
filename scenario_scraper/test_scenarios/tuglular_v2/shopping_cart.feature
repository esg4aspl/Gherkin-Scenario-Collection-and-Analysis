Feature: Shopping cart
	As a visitor of the ecommerce website
	I want to have a shopping cart
	So that I can see the products and costs of what I want to purchase

	Scenario: cart01 - Add a product to cart
		Given product details are displayed #productDetail
		When I select the amount
		And I click add to cart button
		Then the product is added to shopping cart
		And shopping cart page is displayed #shoppingCart

	Scenario: cart02 - Open the shopping cart
		Given home page is displayed #atHome
		When I click shopping cart button
		Then shopping cart page is displayed #shoppingCart