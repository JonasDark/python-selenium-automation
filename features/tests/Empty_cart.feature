# Created by Luttge at 2/21/2022
Feature: Test Scenarios for Amazon Cart
  # Enter feature description here

  Scenario: Verify that no items are in your cart
    Given Open Amazon page
    When Click the cart icon
    Then Verify cart is empty

    

