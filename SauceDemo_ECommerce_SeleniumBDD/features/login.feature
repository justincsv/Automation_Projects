# Execute test cases and generate the report fiels (json)
# behave -f allure_behave.formatter:AllureFormatter -o reports/ features
# allure serve reports/

Feature: SauceDemo Login

    Background: Common steps
        Given SauceDemo homepage is loaded on Chrome browser

    Scenario: Login with a locked out user
        When the user enters username "locked_out_user" and password "secret_sauce"
        And the user clicks on the Login button
        Then an error message is displayed above Login button

    Scenario Outline: Login with multiple parameters
        When the user enters username "<username>" and password "<password>"
        And the user clicks on the Login button
        Then the user is successfully logged in to the Products page

        Examples:
            | username                | password     |
            | standard_user           | secret_sauce |
            | performance_glitch_user | secret_sauce |
            | non_existing_user       | secret_sauce |