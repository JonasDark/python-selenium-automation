# Created by Luttge at 3/5/2022
Feature: Tests for Amazon product page


  Scenario:User can select color options
    Given Open Amazon product Salomon-Cross-Magnet-Black-Punch/dp/B083GRY9FL page
    Then Verify User can click through the colors


  Scenario: User can hover over New Arrivals
    Given Open Amazon product ororo-Lightweight-Heated-Battery-Large/dp/B01H50RF4Q/ref=lp_1045830_1_6 page
    When Hover over New Arrivals tab
    Then Verify options appear