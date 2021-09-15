Feature: Checkout
	As a visitor of the ecommerce website
	I want to be able to do a purchase
	So that I can get the product that I want

	Scenario: check01 - Navigate to checkout
		Given shopping cart page is displayed #shoppingCart
		When I click check out button
		Then check out page is displayed #checkOut

	Scenario: check02 - Successful checkout with existing payment
		Given check out page is displayed #checkOut
		When I select existing address
		And I select existing payment
		And I confirm valid order
		Then “order taken” is displayed #orderConfirmed

	Scenario: check03 - Successful checkout with new payment
		Given check out page is displayed #checkOut
		When I enter a new address
		And I enter new valid payment details
		And I confirm valid order
		Then “order taken” is displayed #orderConfirmed

	Scenario: check04 - Back to order list page
		Given “order taken” is displayed #orderConfirmed
		When I press OK button
		Then order list is displayed #orderList

	Scenario: check05 - Unsuccessful checkout with new payment
		Given check out page is displayed #checkOut
		When I enter a new address
		And I enter new invalid payment details
		And I confirm invalid order
		Then “invalid payment” is displayed #invalidPayment

	Scenario: check06 - Back to checkout page
		Given “invalid payment” is displayed #invalidPayment
		When I press OK button
		Then check out page is displayed #checkOut
