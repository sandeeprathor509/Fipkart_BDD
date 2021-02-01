@flipkart_test
Feature: Flipkart login page

@flipkart_test
Scenario Outline: Logo should pe present at the flipkart home page
    Given Launch the Flipkart website {data/url}
    When Verify the Flipkart logo on the homepage
    Then Verify the visibility of search text field
    Then Enter the value in search box {data/value_to_be_search}
    And Verify the name of the mobile <mobile>
    And Close the browser

        Examples:
        |   mobile                      |
        |   POCO M2 (Slate Blue, 64 GB) |


