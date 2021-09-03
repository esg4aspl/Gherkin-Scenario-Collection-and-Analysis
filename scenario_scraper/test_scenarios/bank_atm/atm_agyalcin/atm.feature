Feature: # Enter feature name here
  # Enter feature description here

  Scenario: atmLogin01 – ATM is idle
    Given I am at the ATM's "Main login page" #loginPage
    When there is no card in the ATM
    Then the ATM displays the "Main login page" #loginPage

  Scenario: atmLogin02 – Insert card with not enough ATM funds
    Given I am at the ATM's "Main login page" #loginPage
    When I inserted my card
    And the ATM has less than the total fund in the ATM at the start of the day
    Then the ATM displays an error message
    And the ATM returns the card #ejectCard

  Scenario: atmLogin03 – Card is ejected after finding that there are not enough funds in the ATM
    Given that I take the card from ATM after ATM displays an error message #
    Then the ATM is redirected to the "Main login page" #loginPage

  Scenario: atmLogin04 – Card is inserted but the information on the card cannot be read
    Given I am at the ATM's "Main login page" #loginPage
    When I inserted my card
    And the information on the card cannot be read Or the card is expired
    Then the ATM displays an error message
    And ATM returns the card #ejectCard

  Scenario: atmLogin05 – Card is inserted and login page is displayed
    Given I am at the ATM's "Main login page" #loginPage
    When I inserted my card
    And the information on the card can be read
    And the card is not expired
    Then the ATM accepts the card
    And the card serial number is logged
    And "Authorization dialog page" is displayed #passwordInputPage

  Scenario: logging01 – Log any message
    Given logging requested
    When message to be logged is ready
    Then the message is logged
    And log file is updated

  Scenario: authorization01 – Valid authorization with password and bank network
    Given the "Authorization dialog page" is displayed #passwordInputPage
    When I enter the password
    And the password is correct
    And the cash card is supported by the ATM
    And there are no problems with the account
    Then authorization is accepted
    And "Main menu" is displayed #mainMenu

  Scenario: authorization02 – Invalid authorization with incorrect password
    Given the "Authorization dialog page" is displayed #passwordInputPage
    When I enter the password
    And the password is incorrect
    And the password is entered wrong for less than three times
    Then authorization is rejected
    And "Wrong password" message is displayed
    And "Authorization dialog page" is displayed
    And the "Wrong password counter" is increased by one #passwordInputPage

  Scenario: authorization03 – Invalid authorization with password being incorrect for more than three times
    Given the "Authorization dialog page" is displayed #passwordInputPage
    When I enter the password
    And the password is incorrect
    And the password is entered wrong for three times
    Then authorization is rejected
    And the card is kept by the ATM
    And the "Wrong password counter" reduced to zero
    And "Call the bank" message is displayed #callTheBankMessageIsDisplayed

  Scenario: authorization04 – Call the bank message is displayed for incorrectly entering the password three times
    Given the "Call the bank" message is displayed #callTheBankMessageIsDisplayed
    When I press Cancel or the OK button
    Then the "Main login page" is displayed #loginPage

  Scenario: authorization05 – Invalid authorization with password being correct but card not being supported
    Given the "Authorization dialog page" is displayed #loginPage
    When I enter the password
    And the password is correct
    And cash card is not supported by the ATM
    Then authorization is rejected
    And card is ejected
    And "Bad bank code" message is displayed #ejectCard

  Scenario: authorization06 – Invalid authorization with problems with the account
    Given the "Authorization dialog page" is displayed #loginPage
    When I enter the password
    And the password is correct
    And there are problems with the account
    Then the authorization is rejected
    And card is ejected
    And "Bad account" message is displayed #ejectCard

  Scenario: authorization07 – Press Cancel at the password input screen
    Given the "Authorization dialog page" is displayed #passwordInputPage
    When I press Cancel
    Then the ATM returns the card #ejectCard

  Scenario: withdrawal01 – Withdrawal menu displayed
    Given the "Main menu page" is being displayed #mainMenu
    When I press the withdrawal button
    Then the "Withdrawal menu" is displayed #withdrawalMenu

  Scenario: withdrawal02 – Valid withdrawal inputs are given
    Given the "Withdrawal menu" being displayed #withdrawalMenu
    When I enter the amount to be withdrawn
    And I press continue button
    And the amount entered is less than "Maximum withdrawal per transaction"
    And the amount entered is less than or equal to the account's balance
    Then the ATM sends the "Withdrawal request" to the bank #withdrawalRequest

  Scenario: withdrawal03 – Bank sends approval response to ATM for withdrawal message
    Given the ATM sends the "Withdrawal request" to the bank #withdrawalRequest
    When the there are no problems with the "Withdrawal request"
    Then the bank sends "Approval message" for "Withdrawal request" #approvalMessageForWithdrawalRequest

  Scenario: withdrawal04 – Bank approves with response
    Given the bank sends "Approval message" for withdrawal request #approvalMessageForWithdrawalRequest
    Then amount of money to be dispensed message is displayed
    And the card is dispensed #cardDispensedBeforeCash

  Scenario: withdrawal05 - Bank denies with approval
    Given the ATM sends the "Withdrawal request" to the bank #withdrawalRequest
    When the there are problems with the "Withdrawal request"
    Then the bank sends "Denied message" for "Withdrawal request" #deniedMessageForWithdrawalRequest

  Scenario: withdrawal06 – ATM redirects to withdrawal menu with deny response from the bank
    Given the bank sends "Denied message" for "Withdrawal request" #deniedMessageForWithdrawalRequest
    Then the error message received from the response of the bank is displayed
    And ATM is redirected to the "Withdrawal menu" #withdrawalMenu

  Scenario: withdrawal07 – ATM dispenses the money after the card is ejected
    Given the card is ejected after withdrawal
    When I take the card from the ATM
    Then the ATM dispenses the money #moneyDispensedFromWithdrawal

  Scenario: withdrawal08 – Money is dispensed for withdrawal
    Given the money is dispensed #moneyDispensedFromWithdrawal
    When I take the money from the ATM
    Then the receipt is printed
    And the amount of money is logged with the serial number of the card
    And the total fund in the ATM value is updated
    And the maximum withdrawal per transaction is updated
    And ATM is redirected to the "Main login page" #loginPage

  Scenario: withdrawal09 – Withdrawal input is taken but input is more than the ATM’s standards
    Given the "Withdrawal menu" being displayed #withdrawalMenu
    When I enter the amount to be withdrawn
    And I press continue button
    And the amount entered is more than "Maximum withdrawal per transaction"
    And the amount entered is less than or equal to the account's balance
    Then "Amount of money to be dispensed is more than the ATM can dispense" message is displayed
    And ATM is redirected to the "Withdrawal menu" #withdrawalMenu

  Scenario: withdrawal10 – Withdrawal input is taken but input is more than the account’s balance
    Given the "Withdrawal menu" being displayed #withdrawalMenu
    When I enter the amount to be withdrawn
    And I press "Continue" button
    And the amount entered is less than "Maximum withdrawal per transaction"
    And the amount entered is more than or equal to the account's balance
    Then "You do not have enough balance for the wanted withdrawal" message is displayed
    And ATM is redirected to the "Withdrawal menu" #withdrawalMenu

  Scenario: withdrawal11 – Withdrawal input is taken but both ATM and account cannot handle the amount
    Given the "Withdrawal menu" being displayed #withdrawalMenu
    When I enter the amount to be withdrawn
    And I press "Continue" button
    And the amount entered is more than "Maximum withdrawal per transaction"
    And the amount entered is more than or equal to the account's balance
    Then "You do not have enough balance for the wanted withdrawal" message is displayed
    And ATM is redirected to the "Withdrawal menu" #withdrawalMenu

  Scenario: withdrawal12 – Press cancel at the withdrawal menu
    Given the "Withdrawal menu" being displayed #withdrawalMenu
    When I press Cancel button
    Then the ATM is redirected to the main menu #mainMenu

  Scenario: moneyTransfer01 – Money transfer menu is displayed
    Given the "Main menu" being displayed #mainMenu
    When I press the transfer money button
    Then the "Money transfer menu" is displayed #moneyTransferPage

  Scenario: moneyTransfer02 – Money transfer input is taken and transfer completed
    Given the "Money transfer menu" being displayed #moneyTransferPage
    When I enter the bank account and amount to be transferred
    And amount is less than or equal to the user's balance
    And receiving account has no problems
    Then the money is transferred
    And the transfer is logged
    And the "Transfer completed message" is displayed #transferCompleteMessageIsDisplayed

  Scenario: moneyTransfer03 – Transfer completed, redirecting to main page
    Given the "Transfer completed message" displayed #transferCompleteMessageIsDisplayed
    When I press the "Continue" or "Cancel" button
    Then I am redirected to the "Main menu" #mainMenu

  Scenario: moneyTransfer04 – Account to be transferred has problems
    Given the "Money transfer menu" being displayed #moneyTransferPage
    When I enter the bank account and amount to be transferred
    And amount is more than the user's balance Or receiving account has problems
    Then the money is not transferred
    And the failed transfer is logged
    And the transfer failed message is displayed #transferFailedMessage

  Scenario: moneyTransfer05 – Transfer failed message and redirecting to main menu
    Given the “Transfer failed message” displayed #transferFailedMessage
    When I press OK or Cancel button
    Then the ATM is redirected to the "Main menu" #mainMenu

  Scenario: moneyTransfer06 – Money transfer input is taken and transfer completed
    Given the "Money transfer menu" being displayed #moneyTransferPage
    When I press Cancel button
    Then the ATM is redirected to the #mainMenu

  Scenario: depositMoneyToATMWithOperator01 – Depositing physical money to ATM
    Given that I am the operator of the ATM
    When I deposit physical money to the ATM by opening the ATM's cash segment and inserting the money
    Then the total amount of money in the ATM is updated

  Scenario: transactions01 – Transactions menu button is pressed
    Given that "Main menu" is being displayed #mainMenu
    When I press the transactions button
    Then "Transactions menu" with the last 10 (or less, if there are less than 10 total transactions) transactions is displayed #transactionsMenu

  Scenario: transactions02 – Transactions menu is displayed
    Given the "Transactions menu" is displayed #transactionsMenu
    When I press "Cancel" or "Return to main menu" button
    Then I am redirected to the "Main menu" #mainMenu

  Scenario: deposit01 – Deposit button is pressed
    Given that "Main menu" being displayed #mainMenu
    When I press deposit button
    Then the "Deposit menu" is displayed #depositMenu

  Scenario: deposit02 – Cash segment is opened after deposit menu is displayed
    Given that the "Deposit menu" is being displayed #depositMenu
    Then the "Cash deposit segment" is opened

  Scenario: deposit03 – Cash is inserted and input has problems
    Given that the "Cash deposit segment" is open #cashDepositSegmentOpened
    When I insert money to the "Cash deposit segment"
    And there are problems with the inserted money
    Then the inserted input is ejected
    And ATM's "Cash deposit segment" is open for deposits #cashDepositSegmentOpened

  Scenario: deposit04 – Cash deposit idle
    Given that the "Cash deposit segment" is open #cashDepositSegmentOpened
    When there is no activity for 30 seconds
    Then the "Cash deposit segment" is closed
    And ATM is redirected to the "Main menu" #mainMenu

  Scenario: deposit05 – Cash is deposited and a confirmation page is displayed
    Given that the "Cash deposit segment" is open #cashDepositSegmentOpened
    When I insert money to the "Cash deposit segment"
    And there are no problems with the input
    Then ATM's cash deposit is closed
    And ATM counts and identifies the money
    And ATM shows a "Deposit confirmation screen" on the ATM #depositConfirmationScreen

  Scenario: deposit06 – Confirming the cash deposit
    Given the "Deposit confirmation screen" #depositConfirmationScreen
    When I press OK
    Then the ATM sends a request to the bank

  Scenario: deposit07 – ATM sends a request to the bank and bank responds with approval message
    Given that ATM sends a request to the bank about depositing #requestSentToBankForDeposit
    Then the bank responds with "Approval message" for deposit #bankRespondsWithApprovalForDeposit

  Scenario: deposit08 – ATM sends a request to the bank and bank responds with denied message
    Given that ATM sends a request to the bank about depositing #requestSentToBankForDeposit
    Then the bank responds with "Denied message" #bankRespondsWithDeniedForDeposit

  Scenario: deposit09 – ATM deposits the money to the account after bank approves
    Given that the bank responds with "Approval message" for deposit #bankRespondsWithApprovalForDeposit
    Then the money is deposited to the account
    And the successful deposit is logged
    And the receipt is printed
    And the ATM is redirected to the "End screen for deposit" #endScreenForDeposit

  Scenario: deposit10 – ATM displays the end screen for deposit
    Given that the ATM is in the "End screen for deposit"  #endScreenForDeposit
    When I press OK or Cancel button
    Then the ATM is redirected to the "Main menu" #mainMenu

  Scenario: deposit11 – ATM denies the request with the denied response coming from bank, deposit input is ejected
    Given that the bank responds with "Denied message for deposit" #bankRespondsWithDeniedForDeposit
    Then the money is ejected from the "Cash dispenser"
    And the failed deposit attempt is logged
    And the ATM is redirected to the "Main menu" #mainMenu

  Scenario: deposit12 – Denying the cash deposit
    Given the "Deposit confirmation screen" #depositConfirmationScreen
    When I press Cancel
    Then the cash is ejected
    And the ATM is redirected to the “Main menu” #mainMenu

  Scenario: deposit13 – Cash is inserted and input has problems
    Given that the "Cash deposit segment" is open #cashDepositSegmentOpened
    When I press Cancel
    Then the Cash Segment is closed
    And ATM is redirected to the “Main menu” #mainMenu

  Scenario: ejectCard01 – Card is ejected
    Given that the card is ejected #ejectCard
    When I take the card
    Then ATM is redirected to the “Main login page” #loginPage

