# Created by emut at 03/09/2021
Feature: A Feature # Enter feature name here
  # Enter feature description here

  Scenario: 01 – Waiting more than 60 seconds after inserting a card
    Given I am on password page #passwordPage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 02 – Waiting more than 60 seconds on home page
    Given I am on home page #homePage
    And I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 03 – Waiting more than 60 seconds on change password page
    Given I am on change password page #changePasswordPage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 04 – Waiting more than 60 seconds after changing password
    Given I changed password #passwordChanged
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 05 – Waiting more than 60 seconds on transfer money page
    Given I am on transfer money page #transferMoneyPage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 06 – Waiting more than 60 seconds after transfer money process
    Given total money is updated #totalMoney
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard


  Scenario: 07 – Waiting more than 60 seconds on inquiryPage
    Given I am on inquiry page #inquiryPage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 08 – Waiting more than 60 seconds on detailed inquiry page
    Given I am on inquiry page #detailedInquiryPage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 09 – Waiting more than 60 seconds on balance inquiry page
    Given I am on inquiry page #balanceInquiryPage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard


  Scenario: 10 – Waiting more than 60 seconds on withdrawal page
    Given I am on inquiry page #withdrawalPage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 11 – Waiting more than 60 seconds on deposit page
    Given I am on inquiry page #depositPage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 12 – Waiting more than 60 seconds when I see error message
    Given I see error message #errorMessage
    When I wait more than 60 seconds
    And ATM swallow the card
    Then the card is frozen #swallowCard


  Scenario: 13 – Insert a valid card into the ATM
    Given I am on login page #loginPage
    When login page is displayed
    And I put valid cash card into the ATM
    Then I am redirected to password page #passwordPage

  Scenario: 14 – Insert a invalid card into the ATM
    Given I am on login page #loginPage
    When login page is displayed
    And I put invalid cash card into the ATM
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 15 – Correct password entrance
    Given I put valid cash card into the ATM #passwordPage
    When password page is displayed
    And I enter correct password
    And I click “Confirm” button
    And home page is displayed
    Then I see options on home page #homePage


  Scenario: 16 – Password correction when wrong password entrance noticed
    Given I put valid cash card into the ATM #passwordPage
    When password page is displayed
    And I notice that I enter wrong password
    And I click “Correction” button
    And I enter correct password
    And I click “Confirm” button
    And home page is displayed
    Then I see options on home page #homePage

  Scenario: 17 – Entered wrong password three times
    Given I put valid cash car into the ATM #passwordPage
    When password page is displayed
    And I enter wrong password three times
    And ATM swallow the card
    Then the card is frozen #swallowCard

  Scenario: 18 – After ATM swallow cash card
    Given the card is frozen #swallowCard
    When login page is displayed
    Then I see login page #loginPage


  Scenario: 19 – Change password page
    Given I am on home page #homePage
    When I click ”Change Password” button
    And change password page is displayed
    Then change password process is started #changePasswordPage

  Scenario: 20 – Back the home page on change password page
    Given I am on change password page #changePasswordPage
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage

  Scenario: 21 – Confirm password changing
    Given I am on Change Password page #changePasswordPage
    When I enter correct original password
    And I enter new password
    And I change password successfully
    Then password is changed #passwordChanged

  Scenario: 22 – Back the home page  after password is changed
    Given I change password #passwordChanged
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage


  Scenario:  23 – Transfer money page
    Given I am on home page #homePage
    When I click ”Transfer money” button
    And transfer money page is displayed
    Then I am on transfer money page #transferMoneyPage

  Scenario: 24 – Back the home page on transfer money page
    Given I am on transfer money page #transferMoneyPage
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage

  Scenario: 25 – Successful transfer money process
    Given I am on transfer money page #transferMoneyPage
    When I enter the appropriate account that I want to transfer money to
    And I enter appropriate amount of money that I want to transfer
    And I click “Confirm” button
    And I see successful transaction message
    Then total money in my account is updated #totalMoney


  Scenario: 26 – Back the home page after successful transaction message is displayed
    Given successful transaction message is displayed #totalMoney
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage

  Scenario: 27 – Unsuccessful transfer money with wrong account
    Given I am on transfer Money page #transferMoneyPage
    When I enter the wrong account that I want to transfer money to
    And error message is displayed
    Then I see error massage #errorMessage

  Scenario: 28 – Unsuccessful transfer money with more amount of money than is in the bank
    Given I am on transfer Money page #transferMoneyPage
    When I enter the appropriate account that I want to transfer money to
    And I enter more amount of money than is in the bank account
    And error message is displayed
    Then I see error massage #errorMessage


  Scenario: 29 – Back the home page after error message is displayed
    Given I see error message #errorMessage
    And I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage

  Scenario: 30 – Inquiry page
    Given I am on home page #homePage
    When I click ”Inquiry” button
    And inquiry page is displayed
    Then I am on inquiry page #inquiryPage

  Scenario: 31 – Back the home page on inquiry page
    Given I am on inquiry page #inquiryPage
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage


  Scenario: 32 – Detailed inquiry page
    Given I am on home page #homePage
    When I click ”Detailed Inquiry” button
    And recent ten transactions details are displayed
    Then I see recent ten transactions details #detailedInquiryPage

  Scenario: 33 – Back the home page on detailed inquiryPage
    Given I am detailed inquiry page #detailedInquiryPage
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage

  Scenario: 34 – Balance inquiry page
    Given I am on home page #homePage
    When I click ”Balance Inquiry” button
    And balance of the account that can be used is displayed
    Then I see balance of the account that can be used #balanceInquiryPage


  Scenario: 35 – Back the home page balance inquiry page
    Given I am on balance inquiry page #balanceInquiryPage
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage

  Scenario: 36 – Withdrawal page
    Given I am on home page #homePage
    When I click ”Withdrawal” button
    And withdrawal page is displayed
    Then withdrawal process is started #withdrawalPage

  Scenario: 37 – Back the home page on withdrawal page
    Given I am on on withdrawal page #withdrawalPage
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage


  Scenario: 38 – Successful withdraw process
    Given I am on transfer Money page #withdrawalPage
    When I enter appropriate amount of money that I want to withdraw
    And I click “Confirm” button
    And I get money from ATM
    And successful transaction message is displayed
    Then total money in my account is updated #totalMoney

  Scenario: 39 – Unsuccessful withdraw process with more amount of money than is in the my account
    Given I am on withdraw money page #withdrawalPage
    When I enter more amount of money than is in the bank account
    And I click “Confirm” button
    And error message is displayed
    Then I see error massage #errorMessage


  Scenario: 40 – Unsuccessful withdraw process with more amount of money is more than maximum withdrawal per day and account
    Given I am on withdraw money page #withdrawalPage
    When I enter more amount of money than maximum withdrawal per day and account
    And I click “Confirm” button
    And error message is displayed
    Then I see error massage #errorMessage

  Scenario: 41– Unsuccessful withdraw process with more amount of money is greater than maximum withdrawal per transaction
    Given I am on withdraw money page #withdrawalPage
    When I enter more amount of money than maximum withdrawal per transaction
    And I click “Confirm” button
    And error massage is displayed
    Then I see error massage #errorMessage


  Scenario: 42 – Unsuccessful withdraw process with more amount of money than is in the ATM
    Given I am on withdraw money page #withdrawalPage
    When I enter more amount of money than is in the ATM
    And I click “Confirm” button
    And error message is displayed
    Then I see error message #errorMessage

  Scenario: 43 – Deposit page
    Given I am on home page #homePage
    When I click ”Deposit” button
    And deposit page is displayed
    Then deposit process is started #depositPage

  Scenario: 44 – Back the home page on deposit page
    Given I am on deposit page #depositPage
    When I click ”Home” button
    And home page is displayed
    Then I see options on home page #homePage


  Scenario: 45 – Successful deposit process
    Given I am on deposit page #depositPage
    When “put the money into the ATM” message is displayed
    And I put the appropriate money into the cover
    And I see successful transaction message
    Then total money in my account is updated #totalMoney

  Scenario: 46 – Unsuccessful deposit with inappropriate money
    Given I am on deposit page #depositPage
    When “put the money into the ATM” message is displayed
    And I put the inappropriate money into the cover
    And error message is displayed
    And I see error massage #errorMessage

  Scenario: 47 – Taking card when user is on homepage
    Given I am on home page #homePage
    When I click ”Take the card” button
    Then I take the cash card #takeCard


  Scenario: 48 – Taking card when user is on password page
    Given I am on password page #passwordPage
    When I click ”Take the card” button
    Then I take the cash card #takeCard

  Scenario: 49 – Login page after taking cash card
    Given I take cash card #takeCard
    And login page is displayed
    Then I am on login page #loginPage

  Scenario: 50 – Finish using ATM after changing password process
    Given I changed password #passwordChanged
    When I want to finish process
    Then process is finished #finishProcess

  Scenario: 51 – Finish using ATM after recent ten transactions details are displayed
    Given I am on detailed inquiry page #detailedInquiryPage
    When I want to finish process
    Then process is finished #finishProcess


  Scenario: 52 – Finish using ATM after balance of the account that can be used is displayed
    Given I am on balance inquiry page #balanceInquiryPage
    When I want to finish process
    Then process is finished #finishProcess

  Scenario: 53 – Finish using ATM after successful transaction message is displayed
    Given successful transaction message is displayed #totalMoney
    When I want to finish process
    Then process is finished #finishProcess

  Scenario: 54 – Finish using ATM after error message is displayed
    Given error message is displayed #errorMessage
    When I want to finish process
    Then process is finished #finishProcess

  Scenario: 55 – Take the cash after finishing process
    Given I finish process #finishProcess
    When process is finished
    Then I take the cash card #takeCard