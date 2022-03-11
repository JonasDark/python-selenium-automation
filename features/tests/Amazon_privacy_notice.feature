# Created by Luttge at 3/8/2022
Feature: Amazon Privacy Notice page tests

  Scenario: Verify user can open and close Amazon Privacy Notice
     Given Open Amazon T&C page
     When Store original windows
     And Click on Amazon Privacy Notice link
     And Switch to newly opened window
     Then Verify Amazon Privacy Notice page is opened
     And User can close new window and switch back to original

