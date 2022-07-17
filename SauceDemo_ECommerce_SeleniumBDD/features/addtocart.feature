Feature: SauceDemo Add To Cart

    Background: Common steps
        Given SauceDemo homepage is loaded on Chrome browser
        When the user enters username "standard_user" and password "secret_sauce"
        And the user clicks on the Login button

    Scenario Outline: Check behavior of add to cart button on products page
        When the user clicks add to cart button on item "<item_index>" in the products page
        Then the add to cart button changes to remove button on item "<item_index>"
        And the product appears in the cart page

        Examples:
            | item_index |
            | 1          |
            | 2          |
            | 3          |
            | 4          |
            | 5          |
            | 6          |

    Scenario Outline: Check behavior of add to cart button on specific product page
        When the user clicks item "<item_index>" in the products page
        And the user clicks add to cart button on specific product page
        Then the add to cart button changes to remove button
        And the product appears in the cart page

        Examples:
            | item_index |
            | 1          |
            | 2          |
            | 3          |
            | 4          |
            | 5          |
            | 6          |

    Scenario: Check behavior of add to cart count ticker increase
        When the user clicks add to cart button in the products page
        Then the cart count ticker increases

    Scenario: Check behavior of add to cart count ticker decrease
        When the user clicks add to cart button in the products page
        And the user clicks remove button
        Then the cart count ticker decreases