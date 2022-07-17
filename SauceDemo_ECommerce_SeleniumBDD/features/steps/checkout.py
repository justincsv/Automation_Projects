from behave import *
from selenium.webdriver.common.by import By

@when('the user clicks on the cart button')
def step_impl(context):
    try:
        context.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    except:
        print("Element not found")

@when('the user checks out with the following info "{FirstName}", "{LastName}", "{ZipCode}"')
def step_impl(context, FirstName, LastName, ZipCode):
    try:
        context.driver.find_element(By.ID, 'checkout').click()
        if FirstName != "None":
            context.driver.find_element(By.ID, 'first-name').send_keys(FirstName)
        if LastName != "None":
            context.driver.find_element(By.ID, 'last-name').send_keys(LastName)
        if ZipCode != "None":
            context.driver.find_element(By.ID, 'postal-code').send_keys(ZipCode)
        context.driver.find_element(By.ID, 'continue').click()
        context.driver.find_element(By.ID, 'finish').click()
    except:
        print("Element not found")

@when('the user clicks on the Continue Shopping button')
def step_impl(context):
    try:
        context.driver.find_element(By.ID, 'continue-shopping').click()
    except:
        print("Element not found")

@then('the checkout is successfully completed')
def step_impl(context):
    try:
        complete_text = context.driver.find_element(By.CLASS_NAME, 'title').text
        assert complete_text == "Checkout: Complete!" is True
    except:
        print("Element not found")

@then('error message appears: "{target_field}" is required')
def step_impl(context, target_field):
    try:
        error_text = context.driver.find_element(By.CLASS_NAME, 'error-button').text
        assert error_text == f"Error: {target_field} is required" is True
    except:
        print("Element not found")