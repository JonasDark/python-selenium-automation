from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class Header(Page):
    ICON = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')
    ORDERS = (By.CSS_SELECTOR, '#nav-orders')
    SELECT_DEPARTMENT = (By.ID, 'searchDropdownBox')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
    DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav[data-category="pet-supplies"]')

    #def verify_correct_department(self):
       # self.wait_for_element_appear(*self.DEPARTMENT)

    def select_department(self, alias):
        select_department = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department)
        select.select_by_value(f'search-alias={alias}')

    def input_search(self, search_word):
        search = self.find_element(*self.SEARCH_INPUT)
        search.clear()
        search.send_keys(search_word)
        # sleep(4)

    def click_search_icon(self):
        self.click(*self.SEARCH_SUBMIT)
        # sleep(1)

    def click_cart_icon(self):
        self.click(*self.ICON)

    def click_orders_button(self):
        self.click(*self.ORDERS)


