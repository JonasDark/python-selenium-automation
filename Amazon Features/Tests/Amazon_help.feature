# Created by Luttge at 2/20/2022
Feature: Test Scenarios for Amazon Help
  # Enter feature description here

  Scenario: Verify Amazon Help Search Field Returns Correct Results
    Given Open Amazon Help Page
    When Input Cancel Items or Orders into search field
    Then Results for Cancel Items or Orders are shown
    # Enter steps here