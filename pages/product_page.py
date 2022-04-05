from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):
    NEW_ARRIVALS_TAB = (By.CSS_SELECTOR, 'a[href*="/New-Arrivals/"]')
    TAB_OPTION = (By.CSS_SELECTOR, '.mm-merch-panel[href*=luggage]')

    def hover_new_arrivals(self):
        tab = self.find_element(*self.NEW_ARRIVALS_TAB)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()

    def open_product_page(self, product_id):
        self.open_page(product_id)

    def verify_new_arrival_option(self):
        self.wait_for_element_appear(*self.TAB_OPTION)


