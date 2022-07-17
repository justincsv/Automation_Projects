Feature: SauceDemo Checkout

    Background: Common steps
        Given SauceDemo homepage is loaded on Chrome browser
        When the user enters username "standard_user" and password "secret_sauce"
        And the user clicks on the Login button
        And the user clicks add to cart button on item "1" in the products page
        And the user clicks on the cart button
    
    Scenario: Successful Checkout
        When the user checks out with the following info "FirstName", "LastName", "100000"
        Then the checkout is successfully completed
    
    Scenario: Checkout with blank information
        When the user checks out with the following info "None", "None", "None"
        Then error message appears: "First Name" is required
    
    Scenario: Checkout with blank Last Name
        When the user checks out with the following info "FirstName", "None", "100000"
        Then error message appears: "Last Name" is required
    
    Scenario: Checkout with blank Postal Code
        When the user checks out with the following info "FirstName", "LastName", "None"
        Then error message appears: "Postal Code" is required
    
    Scenario: Continue shopping
        When the user clicks on the Continue Shopping button
        Then the user is successfully logged in to the Products page

    Scenario: Remove from cart
        When the user clicks remove button
        Then the cart count ticker decreases
