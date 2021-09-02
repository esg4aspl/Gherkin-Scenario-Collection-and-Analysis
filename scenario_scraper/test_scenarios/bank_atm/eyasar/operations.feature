# Created by emut at 02/09/2021
Feature: Operations
  # Enter feature description here

  Scenario: Op01 – select transfer
    Given I am on menu page #operationPage
    When click transfer button
    Then I am redirect to transfer page #transfer

  Scenario: Op02 – select deposit
    Given I am on menu page #operationPage
    When click deposit button
    Then I am redirect to deposit page #deposit

  Scenario: Op03 – select withdraw
    Given I am on menu page #operationPage
    When click withdraw button
    Then I am redirect to withdraw page #withdraw

  Scenario: Op04 – select inquiry
    Given I am on menu page #operationPage
    When click inquiry button
    Then I am redirect to inquiry page #inquiry

  Scenario: Op05 – Transfer money
    Given I am on transfer page #transfer
    When write transfer account number
    And write amount of money
    And click confirm button
    Then atm shows successful message
    And I am redirect to menu page #operationPage

  Scenario: Op06 – Deposit money in the account
    Given I am on deposit page #deposit
    When select the account
    And atm open money entry box
    And put the money on it
    And atm close money entry box
    And atm show amount of money that deposit
    And click confirm button
    Then atm shows successful message
    And I am redirect to menu page #operationPage

  Scenario: Op07 – Withdrawal money
    Given I am on Withdrawal page #withdraw
    When write amount of money that Withdrawal
    And click confirm button
    Then atm gives the money
    And I am redirect to menu page #operationPage

  Scenario: Op08 – Detail inquiry
    Given I am on inquiry page #inquiry
    When select detail inquiry
    Then atm shows recent ten transactions details

  Scenario: Op09 – Balance inquiry
    Given I am on inquiry page #inquiry
    When select balance inquiry
    Then atm shows balance of the account

  Scenario: Op10 – change password
    Given I am on changing password page #changePassword
    When write original password
    And write new password
    And click update button
    Then atm shows the successful message
    And I am redirect to menu page #operationPage








