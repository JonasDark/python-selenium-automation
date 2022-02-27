# Created by Luttge at 2/26/2022
Feature: Tests for Amazon Best Sellers Page

  Scenario: Verify 5 navigation tab links are present
    Given Open Amazon Best Sellers Page
    Then Verify 5 links are present
