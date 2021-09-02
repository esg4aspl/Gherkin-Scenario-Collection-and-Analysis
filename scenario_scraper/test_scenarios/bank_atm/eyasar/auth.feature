# Created by emut at 02/09/2021
Feature: Auth
  # Enter feature description here

  Scenario: Aut01 – Enter right password
    Given I am on password page #passwordPage
    When enter right password
    And click confirm button
    Then I am redirect to menu page #operationPage

  Scenario: Aut02 – Correction password
    Given I am on password page #passwordPage
    When write wrong password
    And click correction password
    Then password clear #passwordPage

  Scenario: Aut03 – Wrong password 3 times
    Given I am on password page #passwordPage
    When write wrong password
    And click confirm button
    And write wrong password again
    And click confirm button
    And write wrong password again
    And click confirm button
    Then account is frozen


