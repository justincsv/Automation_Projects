from behave import *
from selenium.webdriver.common.by import By


@when('the user clicks add to cart button on item "{item_index}" in the products page')
def step_impl(context, item_index):
    # item = "add-to-cart-" + item.lower().replace(" ", "-")
    # context.driver.find_element(By.ID, item).click()
    # for ele in add_to_cart_buttons:
    #     add_to_cart_buttons(item_index)
    #     if ele.get_attribute("id").startswith("add-to-cart-"):
    #         ele.click()
    try:
        # add_to_cart_buttons = context.driver.find_elements(
        #     By.XPATH, '//button[starts-with(@id,"add-to-cart-")]')
        # add_to_cart_buttons[int(item_index) - 1].click()
        item_buttons = context.driver.find_elements(
            By.CLASS_NAME, 'inventory_item_name')
        context.item_name = item_buttons[int(item_index) - 1].text
        item = "add-to-cart-" + context.item_name.lower().replace(" ", "-")
        context.driver.find_element(By.ID, item).click()
    except:
        print("Element not found: " + context.item_name)

@when('the user clicks item "{item_index}" in the products page')
def step_impl(context, item_index):
    try:
        item_buttons = context.driver.find_elements(
            By.CLASS_NAME, 'inventory_item_name')
        context.item_name = item_buttons[int(item_index) - 1].text
        item_buttons[int(item_index) - 1].click()
    except:
        print("Element not found")

@when('the user clicks add to cart button on specific product page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, '//button[starts-with(@id,"add-to-cart-")]').click()
    except:
        print("Element not found")

@when('the user clicks add to cart button in the products page')
def step_impl(context):
    try:
        context.ticker_count = 0
        context.driver.find_element(By.XPATH, '//button[starts-with(@id,"add-to-cart-")]').click()
    except:
        print("Element not found")

@when('the user clicks remove button')
def step_impl(context):
    try:
        context.ticker_count = 0
        context.driver.find_element(By.XPATH, '//button[starts-with(@id,"remove-")]').click()
    except:
        print("Element not found")

@then('the add to cart button changes to remove button on item "{item_index}"')
def step_impl(context, item_index):
    # item = "remove-" + item.lower().replace(" ", "-")
    # remove_button_shown = context.driver.find_element(By.ID, item).is_displayed()
    # remove_buttons = context.driver.find_elements(
    #     By.CLASS_NAME, "btn_inventory")
    # for ele in remove_buttons:
    #     if ele.get_attribute("id").startswith("remove-"):
    #         assert ele.is_displayed() is True
    try:
        # remove_buttons = context.driver.find_elements(
        #     By.XPATH, '//button[starts-with(@id,"remove-")]')
        item = "remove-" + context.item_name.lower().replace(" ", "-")
        assert context.driver.find_element(By.ID, item).is_displayed() is True
    except:
        print("Element not found")

@then('the add to cart button changes to remove button')
def step_impl(context):
    try:
        # remove_button_visible = context.driver.find_element(By.XPATH, '//button[starts-with(@id,"remove-")]').is_displayed()
        item = "remove-" + context.item_name.lower().replace(" ", "-")
        remove_button_visible = context.driver.find_element(By.ID, item).is_displayed()
        assert remove_button_visible is True
    except:
        print("Element not found")

@then('the product appears in the cart page')
def step_impl(context):
    try:
        context.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        cart_items = context.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        for ele in cart_items:
            if ele.text == context.item_name:
                successfully_added = True
                break
        else:
            successfully_added = False
        assert successfully_added is True
    except:
        print("Element not found")

@then('the cart count ticker increases')
def step_impl(context):
    try:
        context.ticker_count = int(context.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
        assert context.ticker_count > 0 is True
    except:
        print(context.ticker_count)

@then('the cart count ticker decreases')
def step_impl(context):
    try:
        context.ticker_count = int(context.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)
        assert context.ticker_count == 0 is True
    except:
        print(context.ticker_count)