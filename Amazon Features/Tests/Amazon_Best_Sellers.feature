# Created by Luttge at 2/26/2022
Feature: Tests for Amazon Best Sellers Page

  Scenario: Verify 5 navigation tab links are present
    Given Open Amazon Best Sellers Page
    Then Verify 5 links are present


  Scenario: Verify 5 Amazon Best Seller page Links open correct page when clicked
    Given Open Amazon Best Sellers Page
    Then Click 5 links and verify correct page is opened

