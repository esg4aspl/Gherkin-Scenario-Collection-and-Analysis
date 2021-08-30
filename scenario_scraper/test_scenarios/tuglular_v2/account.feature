Feature: Account
	As a visitor of the ecommerce website
	I want to be able to see and update my account details
	So that my details for ordering and delivery are correct

	Scenario: acc01 - Login
		Given login page is displayed #loginPage
		When I enter username
		And I enter password
		And I click the login button
		Then home page is displayed #atHome

	Scenario: acc02 - Logout
		Given #atHome
		When I click logout button
		Then login page is displayed #loginPage

	Scenario: acc03 - Account
		Given #atHome
		When I click account button
		Then account page is displayed #account

	Scenario: acc04 - Change payment details
		Given #account
		When I update my payment details
		Then “payment updated” is displayed #paymentUpdated

	Scenario: acc05 - Back to account page
		Given #paymentUpdated
		When I press OK button
		Then account page is displayed #account

	Scenario: acc06 - Change address
		Given #account
		When I update my address
		Then “address updated” is displayed #addressUpdated
	Scenario: acc07 - Back to account page
		Given #addressUpdated
		When I press OK button
		Then account page is displayed #account

	Scenario: acc08 - See orders if any exists
		Given #atHome
		When I go to orders page
		Then order list page is displayed #orderList

	Scenario: acc09 - See order detail of an existing order
		Given #orderList
		When I click on an order
		Then order details are displayed #orderDetail

	Scenario: acc10 - Back to order list page
		Given #orderDetail
		When I press OK button
		Then order list page is displayed #orderList
