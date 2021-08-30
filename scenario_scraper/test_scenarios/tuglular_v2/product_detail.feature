Feature: Product detail page
	As a visitor of the ecommerce website
	I want to see the details of the product
	So that I know if the product fits my needs

	Scenario: pdp01 - Product detail page
		Given #productList
		When I click on a product
		Then product details are displayed #productDetail

	Scenario: pdp02 - Product detail page
		Given #filteredProductList
		When I click on a product
		Then product details are displayed #productDetail