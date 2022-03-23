from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    ICON = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')
    ORDERS = (By.CSS_SELECTOR, '#nav-orders')

    def click_cart_icon(self):
        self.click(*self.ICON)

    def click_orders_button(self):
        self.click(*self.ORDERS)


