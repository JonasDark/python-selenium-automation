# Created by Luttge at 3/6/2022
Feature: Whole Foods Deals page


  Scenario: Verify word in product name
    Given Open Amazon Deals page
    Then Verify word Regular is present under product

    # Enter steps here