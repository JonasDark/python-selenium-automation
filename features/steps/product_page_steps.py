from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


CURRENT_COLOR = (By.CSS_SELECTOR, 'div.a-row span.selection')
COLOR_OPTIONS = (By.CSS_SELECTOR, 'ul.swatches.swatchesSquare.imageSwatches li')


@given('Open Amazon product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/{product_id}/')


@then('Verify User can click through the colors')
def verify_color_clicks(context):
    expected_colors = ['Goji Berry/Black/Red Orange', 'Magnet/Black/Lime Punch', 'Phantom/Black/Ebony', 'Multi']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(color_options)):
        print('i:', i)
        color_options[i].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('current_color:', current_color)
        assert current_color == expected_colors[i]

