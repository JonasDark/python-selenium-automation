from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


five_links = (By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a")
EXPECTED_NAMES = ['Amazon Best Sellers', 'Amazon Hot New Releases', 'Amazon Movers & Shakers', 'Amazon Most Wished For',
                  'Amazon Gift Ideas']
CURRENT_PAGE = (By.CSS_SELECTOR, 'span#zg_banner_text')
CLICKABLE_LINKS = (By.CSS_SELECTOR, '#zg_header li a')


@given('Open Amazon Best Sellers Page')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify 5 links are present')
def verify_links(context):
    links = context.driver.find_elements(*five_links)
    print(links)
    assert len(links) == 5, f'expected 5 links but instead got {len(links)}'


@then('Click 5 links and verify correct page is opened')
def click_and_verify(context):
    click_link = context.driver.find_elements(*CLICKABLE_LINKS)
    for i in range(len(click_link)):
        # context.driver.refresh()
        # context.driver.wait.until(EC.element_to_be_clickable(CLICKABLE_LINKS))
        click_link = context.driver.find_elements(*CLICKABLE_LINKS)
        click_link[i].click()
        # context.driver.wait.until(EC.presence_of_element_located(CURRENT_PAGE))
        current_page = context.driver.find_element(*CURRENT_PAGE).text
        assert current_page == EXPECTED_NAMES[i], 'Text not expected'
        if current_page == EXPECTED_NAMES[-1]:
            print('Success!!!')



