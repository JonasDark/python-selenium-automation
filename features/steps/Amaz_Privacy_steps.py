from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Amazon Privacy Notice page is opened')
def verify_page_open(context):
    actual_words = context.driver.find_element(By.CSS_SELECTOR, 'div.cs-help-content div.help-content h1').text
    expected_words = 'Amazon.com Privacy Notice'
    assert expected_words == actual_words, 'Expected words not found'


@then('User can close new window and switch back to original')
def switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
    context.driver.find_element(By.CSS_SELECTOR, 'div.help-service-content p a[href*=privacy]')

