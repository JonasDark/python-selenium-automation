from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

Search_Input = (By.ID, 'helpsearch')


@given('Open Amazon Help Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId'
                       '=508088')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*Search_Input)
    search.clear()
    search.send_keys(search_word)
    search.send_keys(Keys.RETURN)


@then('Results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text
    assert expected_result == actual_result, f'Expected text {expected_result} did not match {actual_result}'


print("test case passed")
