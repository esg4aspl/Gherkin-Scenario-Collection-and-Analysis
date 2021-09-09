# Created by emut at 07/09/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: init 01 – Successful initialize
    Given ATM on Operator Panel
    When ATM switched on
    And Initial cash entered
    And Set maximum withdraw per day for an account
    And Set maximum and minimum withdraw per transaction
    And Open Connection to the bank network
    Then the atm is initialized and navigated to welcomePage #welcomePage

  Scenario: init 02 – Unsuccessful initialize
    Given ATM on Operator Panel
    When ATM switched on
    And An error occured
    Then The error captured and prints error details

  Scenario: reader 01 – Read Card
    Given I am at welcomePage and I entered the bank card #welcomePage
    When card number is valid
    And account number is found
    And serial number log is sent
    Then Card read is completed and navigated to loginPage #loginPage

  Scenario: reader 02 – Eject Card
    Given I am at welcomePage and I entered the bank card #welcomePage
    When card is invalid
    And card read error log is sent
    Then Eject card and navigate to welcomePage #welcomePage


  Scenario: reader 03 – Retain Card
    Given I am at welcomePage and I entered the bank card #welcomePage
    And Card is expired
    And  card expire log is send
    Then Retain card and navigate to welcomePage #welcomePage

  Scenario: login 01 – Successful Login
    Given I am at loginPage #loginPage
    When I entered password
    And password is correct
    And session is set with card and account details
    Then Login sucessful and then navigate to homePage #homePage

  Scenario: login 02 – Unsuccessful Login Opeation
    Given I am at loginPage #loginPage
    When I entered wrong password
    And Error message displayed on console out
    Then Login operation is unsuccessful and still in the loginPage #loginPage

  Scenario: login 03 – Login Card Block
    Given I am at loginPage #loginPage
    When I entered 3 times wrong password
    And Card retain message is displayed on console out
    And Card retained by atm
    Then Login operation is unsuccessful and navigate to welcomePage #welcomePage

  Scenario: operations 01 – Display operations list
    Given I am at homePage and session is active #homePage
    When operation list displayed on the app console
    And operation countdown timer is started
    Then Atm is ready to read operation choice


  Scenario: operations 02 – Successful Transfer transaction
    Given I am at homePage and session is active #homePage
    When option 1 is selected for transfer operation
    And transfer account(to) is entered
    And transfer amount is entered
    And account(from) balance is available
    And transfer transaction is completed
    And receipt printed to console
    And available cash is updated
    And session timer is refreshed
    Then Operation list is displayed and ready to next choice

  Scenario: operation 03: - Unsuccessful Transfer transaction
    Given I am at homePage and session is active #homePage
    When transfer account(to) is entered
    And transfer amount is entered
    And amount is invalid(not enough balance)
    And error message is displayed on the console
    Then ready to read new transfer amount

  Scenario: operation 04: - Successful Inquiry transaction
    Given I am at homePage and session is active #homePage
    When option 2 is selected for inquiry operation
    And account balance is retrieved
    And receipt printed to console
    And session timer is refreshed
    Then Operation list is displayed and ready to next choice

  Scenario: operations 05 – Successful Withdraw transaction
    Given I am at homePage and session is active #homePage
    When option 3 is selected for withdraw operation
    And withdraw amount is entered
    And account balance is available
    And withdraw completed
    And available cash is updated
    And receipt printed to console
    And session timer is refreshed
    Then Operation list is displayed and ready to read next choice

  Scenario: operations 06 – Unsuccessful Withdraw transaction
    Given I am at homePage and session is active #homePage
    When option 3 is selected for withdraw operation
    And withdraw amount is entered
    And amount is invalid(out of account or atm limits)
    And error message is displayed on the console
    Then ready to read new withdraw amount

  Scenario: operations 07 – Successful Deposit transaction
    Given I am at homePage and session is active #homePage
    When option 4 is selected for deposit operation
    And deposit amount is entered
    And deposit completed
    And receipt printed to console
    And session timer is refreshed
    Then Operation list is displayed and ready to read next choice

  Scenario: operations 08 – Unsuccessful Deposit transaction
    Given I am at homePage and session is active #homePage
    When option 4 is selected for deposit operation
    And deposit amount is entered
    And amount is invalid(out of daily limit)
    And error message is displayed on the console
    Then ready to read new deposit amount

  Scenario: operations 09: Logout
    Given I am at homePage and session is active #homePage
    When option 5 is selected for exit operation;
    And session is cleared
    And logout message is displayed to console
    And eject card
    Then Logout operation is successful and navigate to #welcomePage


  Scenario: operations 10: Session time out
    Given I am at homePage and session is active #homePage
    When 60 seconds after session timer is out of clock
    And session is cleared
    And timeout message is displayed to console
    And eject card
    Then Logout operation is successful and navigate to welcomePage #welcomePage