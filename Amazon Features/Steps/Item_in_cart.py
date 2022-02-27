from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
SEARCH_SUBMIT = (By.CSS_SELECTOR, '#nav-search-submit-button')
ITEM = (By.XPATH, '//span[@data-component-type="s-search-results"]//a[.//span[@class="a-price"]]')
ADD_ITEM_CART = (By.CSS_SELECTOR, '#add-to-cart-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()


@when('Click item')
def click_item(context):
    context.driver.find_element(*ITEM).click()


@when('Add item to cart')
def add_item(context):
    context.driver.find_element(*ADD_ITEM_CART).click()


@then('Verify {expected_result} item was added to cart')
def cart_num(context, expected_result):
    # expected_result = '1'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div#nav-cart-count-container span').text
    assert expected_result == actual_result, f'Expected result of {expected_result} did not match {actual_result}'














