# Created by Luttge at 3/23/2022
Feature: Amazon Main Page
  # Enter feature description here

  Scenario: Verify clicking 'Orders' button opens 'Sign-In' page
    Given Open Amazon main page
    Then Click 'Orders' button
    Then Verify 'Sign-In' page opens
