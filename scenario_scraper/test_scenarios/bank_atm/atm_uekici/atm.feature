# Created by emut at 30/08/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: afr1_2
    # Enter steps here
    Given ATM is in initial state #initialState
    When initial parameters given
    Then ATM must show the welcome screen #welcome

  Scenario: afr3
    Given withdraw is completed #withdrawCompleted
    When ATM is out of money
    Then ATM should display out of money error screen #outOfMoney

  Scenario: afr4
    Given ATM is in welcome screen #welcome
    When User inserts invalid card
    Then card invalid error is displayed
    And card is returned
    And ATM goes back to welcome screen #welcome

  Scenario: afr5_6
    Given ATM is in welcome screen #welcome
    When User inserts valid card
    Then authorization dialog is initiated #authScreen

  Scenario: afr7
    Given ATM is in authorization screen #authScreen
    When user enters the password
    Then account info and password passed to Bank #authReqToBank

  Scenario: afr8
    Given ATM is waiting authorization from Bank
    And auth fails #authFailRespFromBank
    Then ATM ejects the card
    And ATM displays error message
    And ATM goes back to welcome screen #welcome

  Scenario: afr9
    Given ATM is waiting authorization from Bank
    And auth succeeds #authRespOkFromBank
    Then ATM initiates transaction dialog #initTransaction

  Scenario: afr10
    Given ATM is waiting authorization from Bank
    And Bank orders to retain the user card #authRespRetainFromBank
    Then ATM displays error message
    And ATM keeps the card
    And ATM goes back to welcome screen #welcome

    Scenario: afr11
    Given ATM is in transaction screen #initTransaction
    When User enters an amount out of the limit
    Then ATM displays error message
    And ATM goes back to transaction screen #initTransaction

    Scenario: afr12_13
    Given ATM is in transaction screen #initTransaction
    When User enters an amount within the limit
    Then ATM sends transaction request to Bank #transactionReqToBank

    Scenario: afr14-1
    Given ATM waiting transaction response from Bank
    And ATM sends OK #transactionRespOKFromBank
    Then ATM prints receipt
    And ATM updates total funds
    And ATM ejects the card
    And ATM displays do not forget card screen #cardEjectedBeforeMoney

Scenario: afr14-2_15-1
    Given ATM displays do not forget card screen #cardEjectedBeforeMoney
    When user takes the card
    Then ATM dispenses the money
    And ATM logs amount of dispensed money
    And ATM notifies Bank on the dispensed money #notifyBankOnWithdraw

Scenario: afr15_2
    Given ATM waiting transaction notification response #waitWithdrawNotfResp
    Then transaction is completed #withdrawCompleted

Scenario: afr15_3
    Given withdraw is complete #withdrawCompleted
    When ATM has enough money
    Then ATM goes back to welcome screen #welcome

Scenario: afr16
    Given ATM waiting transaction response from Bank
    And ATM sends Failed #transactionRespFailFromBank
    Then ATM displays error message
    And ATM ejects the card
    And ATM goes back to welcome screen #welcome

Scenario: bfr1-2:
    Given Bank receives #authReqToBank
    When card is not issued by Bank
    Then Bank returns failure to authenticate #authFailRespFromBank

Scenario: bfr3:
    Given Bank receives #authReqToBank
    When card is issued by Bank
    Then Bank proceeds with authentication #bankAuth

Scenario: bfr4_1:
    Given Bank is in authentication state #bankAuth
    When password is invalid
    Then Bank returns failure #authFailRespFromBank

Scenario: bfr4_2:
    Given Bank is in authentication state #bankAuth
    When password is valid
    Then Bank proceeds #checkAccountStatus

Scenario: bfr5
    Given Bank is in account status check step #checkAccountStatus
    When account has problems
    Then Bank returns bad account to ATM #authRespRetainFromBank

Scenario: bfr6
    Given Bank is in account status check step #checkAccountStatus
    When account has no problems
    Then Bank returns OK to ATM #authRespOkFromBank

Scenario: bfr7_1
    Given Bank received a transaction request #transactionReqToBank
    When transaction is denied
    Then Bank returns rejected to ATM #transactionRespFailFromBank

Scenario: bfr7_2
    Given Bank received a transaction request #transactionReqToBank
    When transaction is approved
    Then Bank returns OK to ATM #transactionRespOKFromBank

Scenario: bfr8
    Given Bank received transaction notification #notifyBankOnWithdraw
    Then update account with transaction
    And return OK to ATM #waitWithdrawNotfResp
