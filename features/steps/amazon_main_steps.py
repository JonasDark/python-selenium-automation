from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon Main Page')
def open_amazon(context):
    context.app.amazon_main_page.open_amazon_main()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.app.header.input_search(search_word)


@when('Search for {search_word} in department')
def input_search(context, search_word):
    context.app.header.input_search(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.app.header.click_search_icon()
    # sleep(1)


@then("Click 'orders' button")
def click_orders_button(context):
    context.app.header.click_orders_button()


@then("Verify 'Sign-In' page opens")
def verify_signin(context):
    context.app.signin_page.verify_signin_page()

'''
@then('Verify Pet Supplies department selected')
def verify_correct_department(context):
    context.app.header.verify_correct_department()
'''





