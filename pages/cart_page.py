from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    actual_text = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']//h2")
    expected_text = 'Your Amazon Cart is empty'

    def verify_txt(self):
        self.verify_text(self.expected_text, *self.actual_text)

