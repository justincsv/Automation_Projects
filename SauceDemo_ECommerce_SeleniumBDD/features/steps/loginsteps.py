from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('SauceDemo homepage is loaded on Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.driver.get("https://www.saucedemo.com/")


@when('the user enters username "{user}" and password "{pw}"')
def step_impl(context, user, pw):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pw)


@when('the user clicks on the Login button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('the user is successfully logged in to the Products page')
def step_impl(context):
    try:
        page_loaded = context.driver.find_element(
            By.ID, "shopping_cart_container").is_displayed()
    except:
        context.driver.close()
        assert False, "Was not successfully logged in"

    if page_loaded:
        context.driver.close()
        assert True


@then('an error message is displayed above Login button')
def step_impl(context):
    try:
        error_displayed = context.driver.find_element(
            By.CLASS_NAME, "error-button").is_displayed()
    except:
        context.driver.close()
        assert False, "Error message must be displayed"

    if error_displayed:
        context.driver.close()
        assert True
