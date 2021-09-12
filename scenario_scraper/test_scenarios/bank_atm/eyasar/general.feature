# Created by emut at 02/09/2021
Feature: General
  # Enter feature description here

  Scenario: Gen01 – Check invalid cash card
    Given I am in front of atm #userArrived
    When insert the invalid cash card in to the atm
    Then atm shows error message
    And return cash card #cardEjected

  Scenario: Gen02 – Check valid cash card
    Given I am in front of atm #userArrived
    When insert the valid cash card in to the atm
    Then I am redirect to password page #passwordPage

  Scenario: Gen03 – Take the card
    Given I am on password page #passwordPage
    When click take card button
    Then atm gives me the cash card #cardEjected

  Scenario: Gen04 – Take the card on operation page
    Given I am on menu page #operationPage
    When click take card button
    Then atm gives me the cash card #cardEjected


  # tags are missing in these scenarios!