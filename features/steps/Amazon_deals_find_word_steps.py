from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_LABELS = (By.XPATH, "//li[@class = 's-result-item' and .//span[contains (@class, 'prime-price')]]/div")
PRODUCT_NAME = (By.CSS_SELECTOR, 'ul.s-result-list li div.s-item-container .wfm-sales-item-card__product-name')


@given('Open Amazon Deals page')
def open_deals(context):
    context.driver.get("https://www.amazon.com/fmc/storedeals/?_encoding=UTF8&almBrandId=VUZHIFdob2xlIEZvb2Rz")


@then('Verify word Regular is present under product')
def verify_text(context):
    actual_word = context.driver.find_elements(*PRODUCT_LABELS)

    for i in actual_word:
        assert 'Regular' in i.text, f'Expected the word Regular in element'

        product_name = i.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, 'Expected product name text in element'




