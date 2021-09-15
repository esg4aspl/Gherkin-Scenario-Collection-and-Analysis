Feature: Search
	As a visitor of the ecommerce website
	I want to search for products
	So that I can quickly find what I am looking for

	Scenario: search01 - Search with a single keyword
		Given home page is displayed #atHome
		When I enter single keyword
		And I click search button
		Then search result page is displayed #productList

	Scenario: search02 - Search with multiple keywords
		Given home page is displayed #atHome
		When I enter multiple keywords
		And I click search button
		Then search result page is displayed #productList