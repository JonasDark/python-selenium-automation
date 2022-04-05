# Created by Luttge at 3/23/2022
Feature: Amazon Main Page
  # Enter feature description here

  Scenario: Verify clicking 'Orders' button opens 'Sign-In' page
    Given Open Amazon main page
    Then Click 'Orders' button
    Then Verify 'Sign-In' page opens


  Scenario Outline: Verify user can select and search in a department
    Given Open Amazon Main Page
    When select department by alias <alias>
    And Search for <search_word> in department
    And Click on search icon
    Then Verify <department> department selected
    Examples:
    |  alias        |  search_word  |  department  |
    |  pets         |  cat tower    |  pet-supplies|
    |  stripbooks   |  nietschze    |  books       |
    |  popular      |  iron maiden  |  music       |
