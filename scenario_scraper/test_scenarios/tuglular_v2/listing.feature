Feature: Product list page
	As a visitor of the ecommerce website
	I want to see an overview of products
	So that I can select a product that fits my needs

	Scenario: plp01 - Navigate to a product list page
		Given home page is displayed #atHome
		When I select a product list page from the menu
		Then product list page is displayed #productList

	Scenario: plp02 - Filter on the product list page
		Given product list page is displayed #productList
		When I select a filter
		And I click the filter button
		Then filtered products are displayed #filteredProductList