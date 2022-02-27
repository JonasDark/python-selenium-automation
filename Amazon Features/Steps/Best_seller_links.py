from selenium.webdriver.common.by import By
from behave import given, when, then

five_links = (By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a")


@given('Open Amazon Best Sellers Page')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify 5 links are present')
def verify_links(context):
    links = context.driver.find_elements(*five_links)
    print(links)
    assert len(links) == 5, f'expected 5 links but instead got {len(links)}'

