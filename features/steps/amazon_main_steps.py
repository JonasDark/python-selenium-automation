from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon Main Page')
def open_amazon(context):
    context.app.amazon_main_page.open_amazon_main()


@then("Click 'orders' button")
def click_orders_button(context):
    context.app.header.click_orders_button()


@then("Verify 'Sign-In' page opens")
def verify_signin(context):
    context.app.signin_page.verify_signin_page()








