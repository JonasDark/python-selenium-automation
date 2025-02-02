from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.app.amazon_main_page.open_amazon_main()
    # context.driver.get('https://www.amazon.com/')


@when('Click the cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()
    # context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()


@then('Verify cart is empty')
def verify_cart(context):
    context.app.cart_page.verify_txt()
    # expected_result = 'Your Amazon Cart is empty'
    # actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']//h2").text
    # assert expected_result == actual_result, f'Expected text {expected_result} did not match {actual_result}'






