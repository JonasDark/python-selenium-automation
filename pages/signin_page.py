from selenium.webdriver.common.by import By
from pages.base_page import Page


class SigninPage(Page):
    SIGNIN = (By.CSS_SELECTOR, )

    def verify_signin_page(self):
        self.verify_url_contains_query('signin')

