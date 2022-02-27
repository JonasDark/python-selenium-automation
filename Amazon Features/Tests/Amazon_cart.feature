# Created by Luttge at 2/26/2022
Feature: Amazon Cart Page


  Scenario: Verify item added to cart
    Given Open Amazon Page
    When Search for gloves
    And Click on search icon
    And Click Item
    And Add item to cart
    Then Verify 1 item was added to cart
